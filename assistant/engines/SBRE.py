import importlib.util
import os

#from assistant.components.memory import Memory, WorkingMemory

from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor

class SkillBasedResponseEngine:
    """
        The primary, most recommended esponse engine built around modularity and utility.
    """

    def __init__(self, assistant):

        # An instance of the assistant.
        self.assistant = assistant

        self.log = self.assistant.logger # alias for logger
        self.config = self.assistant.config['engine']['sbre']  # alias for engine config

        # Path where active skills are located.
        # todo: Make this a list.
        self.active_skills_path = os.path.join(assistant.cwd, "skills", "active")
        self.active_skills = {}

        # Path where the passive skills are located.
        self.passive_skills_path = os.path.join(assistant.cwd, "skills", "passive")
        self.passive_skills = {}
        
        self.load_active_skills()

    def __call__(self, msg:Message):
        return self.process(msg)
    
    # try..except
    def load_active_skill(self, skill_name, skill_path):
        try:
            spec = importlib.util.spec_from_file_location(skill_name, skill_path)
            skill = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(skill)
            #sys.modules["module.name"] = foo
            self.active_skills[skill_name] = skill.setup(self.assistant)

            self.log.info(f"Loaded Skill '{skill_name}' from {skill_path}")
        except Exception as ex:
            self.log.warning(f"Loading '{skill_name}' failed due to: {ex}")
    
    def load_active_skills(self):
        for subdir, dirs, files in os.walk(self.active_skills_path):
            for file in files:
                if file.endswith('main.py'):
                    name = subdir[subdir.rindex('\\') + 1:]  # todo: Change for linux
                    path = os.path.join(subdir, file)
                    self.load_active_skill(name, path)

    def process(self, msg:Message):
        # Figure out what skills are triggered by the input.
        matches = []
        for skill_id, skill in self.active_skills.items():
            result = skill.evaluate(msg)
            
            self.log.info(f"\t[SKILL ACTIVATION] {skill_id}: {result * 100}% Confidence")

            # Log the skill only if the evaluation is accurate enough.    
            if result >= self.config['accuracy']:
                # Log the skill + confidence
                matches.append((skill_id, result))

        if not matches:
            out = SentenceConstructor([
                [
                    ("I'm sorry,", "Sorry,", ''),
                    ("I could not", "I'm unable to", "I don't"),
                    ("understand.")  # , "catch that"
                ]
            ])

            return Response('NOT-OK', out.generate())

        # Sort the matches by confidence so we know which is the most accurate skill to trigger.
        matches.sort(key = lambda x: x[1], reverse = True)

        if self.config['allow_multi_activation']:
            outputs = []
            for skill_id, confidence in tuple(matches):
                output = self.active_skills[skill_id].process(msg)
                
                outputs.append(output)
            return outputs
        else:
            return self.active_skills[matches[0][0]].process(msg)

class Skill:
    def __init__(self, assistant):
        
        # An instance of the assistant to access components such as memory.
        self.assistant = assistant

        # PatternExpression items that inputs are supposed to be checked against.
        self.patterns = []

        # Whether the skill is awaiting secondary input from the user.
        # For eg:
        # Who is Alan Turing?
        # >> (Answer) -> awaiting_input
        # Why was he famous? -> Why was [Alan Turing] famous?
        # >> 
        self.awaiting_input = False

        # todo pull context from self.assistant.memory.pull_context(self)

    def _on_skill_load(self):
        pass

    def _on_skill_unload(self):
        pass

    def evaluate(self, message:Message):
        """Matches the skill patterns with message."""
        confidence = 0
        for pattern in self.patterns:
            conf = pattern.match(message)
            if conf > confidence:
                confidence = conf
        return confidence

    def process(self, message:Message):
        raise NotImplemented

    def reset(self):
        pass