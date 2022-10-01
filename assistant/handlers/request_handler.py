from assistant.datatypes.message import Message
from assistant.engines import SRE, SBRE

class RequestHandler:
    def __init__(self, interpreter):
        
        # Get the instance of the intent interpreter.
        self.interpreter = interpreter

        # Get the instance of the assistant.
        self.assistant = interpreter.assistant

        # Get the instance of the logger.
        self.logger = self.assistant.logger

        # Skill-Based Response Engine (SBRE) is the modular and extendable response engine.
        self.engine = SBRE.SkillBasedResponseEngine(self)
    
    # todo: def load_engine, unload_engine, reload_engine, set_engine
    
    def handle(self, message):
        msg = Message(message)
        return self.engine(msg)
    
    def check(self, message):
        return True