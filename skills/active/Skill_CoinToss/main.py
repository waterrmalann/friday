from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor
from assistant.processing.pattern_expression import PatternExpression
from assistant.engines import SBRE

class Skill_CoinToss(SBRE.Skill):
    def __init__(self, assistant):
        super().__init__(assistant)

        self.patterns = [
            PatternExpression([
                ("flip", "toss", "throw"),
                {'a', },
                ("coin", "penny", "dime", "nickel")
            ])
        ]

    def process(self, message:Message):
        reply = SentenceConstructor()
        reply.add_syntax([
            "I",
            ("flipped", "tossed", "threw"),
            ("a coin", "a penny"),
            ("and got", "and its", ", its", ", got"),
            ("heads", "tails")
        ])
        reply.add_syntax([
            ("heads", "tails"),
            "it is"
        ])
        reply.add_syntax([
            "I got",
            ("heads", "tails")
        ])

        return Response('OK', reply.generate())

def setup(assistant):
    return Skill_CoinToss(assistant)