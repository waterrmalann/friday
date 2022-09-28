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

    def process(self, message:Message):
        
        reply = SentenceConstructor()

        # Check if a natural number is in the string.
        pe = PatternExpression([2])
        if pe.match(message):
            num = pe.extract(message)[MessageTokens.NaturalNumber]
            result = random.randint(1, num)

            reply.add_syntax([
                "I rolled a {number}-sided die",
                ("and got", "and its", ", its", ", got"),
                "{result}"
            ])

            out = reply.generate(result=result, number=num)
        else:
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