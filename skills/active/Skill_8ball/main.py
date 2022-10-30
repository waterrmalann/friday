from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor
from assistant.processing.pattern_expression import PatternExpression
from assistant.engines import SBRE

import json
import random
import os

class Skill_8ball(SBRE.Skill):
    def __init__(self, assistant, ctx):
        super().__init__(assistant, ctx)

        self.patterns = [
            PatternExpression([
                ("8ball", "8-ball", "eight-ball", "eightball")
            ])
        ]

        with open(os.path.join(self.ctx['root_path'], 'data', 'responses.json')) as f:
            self.responses = json.load(f)

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

def setup(assistant, ctx):
    return Skill_8ball(assistant, ctx)