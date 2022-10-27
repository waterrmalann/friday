from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor
from assistant.processing.pattern_expression import PatternExpression
from assistant.engines import SBRE

import json
import random

class Skill_8ball(SBRE.Skill):
    def __init__(self, assistant, responses):
        super().__init__(assistant)

        self.patterns = [
            PatternExpression([
                ("8ball", "8-ball", "eight-ball", "eightball")
            ])
        ]
        
        self.responses = responses

    def process(self, message:Message):
        fortune_type = random.choice(list(self.responses))
        fortune = random.choice(self.responses[fortune_type])

        reply = SentenceConstructor()
        reply.add_syntax([
            ("8-ball says:", "Magic 8-Ball says,"),
            '"{fortune}"'
        ])
        reply.add_syntax([
            "{fortune}"
        ])

        out = reply.generate(fortune=fortune)

        return Response('OK', out)

def setup(assistant):
    with open('skills/active/Skill_8ball/data/responses.json') as f:
        responses = json.load(f)
    return Skill_8ball(assistant, responses)