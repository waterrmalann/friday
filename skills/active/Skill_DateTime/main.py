from assistant.datatypes.message import Message
from assistant.datatypes.response import Response
from assistant.processing.sentence_constructor import SentenceConstructor
from assistant.processing.pattern_expression import PatternExpression
from assistant.engines import SBRE

import datetime
from assistant.utils.formatters import int_suffix

class Skill_DateTime(SBRE.Skill):
    """
        Information regarding current date and time.
    """

    def __init__(self, assistant, ctx):
        super().__init__(assistant, ctx)

        self.patterns = [
            PatternExpression([
                {"what", },
                ("day", "time", "date", "year")
            ])
        ]

    def process(self, message:Message):
        reply = SentenceConstructor()

        # todo: tbh just match for "year" 
        if PatternExpression([("year is it", "year it is")]).match(message):
            # eg: What year is it?

            year = datetime.datetime.now().year
            reply.add_syntax([
                ("It's", "You're living in", "The year is"),
                "{}"
            ])
            return Response('OK', reply.generate(year))

        elif PatternExpression([("day is it", "day it is", "day")]).match(message):
            # eg: What day is it?

            now = datetime.datetime.now()
            day = int_suffix(now.day)
            # datetime.datetime.now().strftime("The date is %d %B %Y. It's a %A")
            day_name = now.strftime("%A")
            month_name = now.strftime("%B")

            reply.add_syntax([
                ("It's a", "It's"),
                "{day_name},",
                {"the", },
                "{day} of {month_name}"
            ])
            reply.add_syntax([
                "It's",
                ("{month_name} {day}, {day_name}", "{day} of {month_name}, {day_name}"),
            ])
            
            return Response('OK', reply.generate(day=day, month_name=month_name, day_name=day_name))

        else:
            # What's the date?

            now = datetime.datetime.now()
            year = now.year
            day = int_suffix(now.day) # 23rd
            day_name = now.strftime("%A")  # Tuesday
            month_name = now.strftime("%B")  # September
            # It is Tuesday, September 24th, 2004

            reply.add_syntax([
                ("It is", "It's"),
                ("{day_name}, {month_name} {day}, {year}", "{day_name}, {day} of {month_name}, {year}")
            ])

            return Response('OK', reply.generate(day_name=day_name, month_name=month_name, year=year, day=day))

def setup(assistant, ctx):
    return Skill_DateTime(assistant, ctx)