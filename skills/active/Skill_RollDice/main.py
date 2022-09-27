from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor
from assistant.processing.pattern_expression import PatternExpression
from assistant.engines import SBRE

import random

class Skill_RollDice(SBRE.Skill):
    def __init__(self, assistant):
        super().__init__(assistant)

        self.patterns = [
            PatternExpression([
                ("roll", "throw", "toss"),
                {'a', },
                ("dice", "die")
            ])
        ]

    def process(self, message:Message):
        reply = SentenceConstructor()
        reply.add_syntax([
            "I rolled",
            ("a dice", "a die"),
            ("and got", "and its", ", its", ", got"),
            "{}"
        ])
        reply.add_syntax([
            "{}",
            "it is"
        ])
        reply.add_syntax([
            "I got",
            "{}"
        ])

        # Roll a six-sided die.
        result = random.randint(1, 6)
        out = reply.generate(result)

        return Response('OK', out)

def setup(assistant):
    return Skill_RollDice(assistant)