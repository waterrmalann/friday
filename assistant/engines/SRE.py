import datetime
import random
from assistant.datatypes.message import Message
from assistant.datatypes.response import Response

class SimpletonResponseEngine:
    """A super simple response engine for demonstration purposes."""

    def __init__(self, assistant):
        # An instance of the assistance.
        self.assistant = assistant 
    
    def __call__(self, msg:Message):
        cmd = msg.processed
        cmd_tokens = msg.tokenized

        # What is the time?
        if "time" in cmd:
            time = datetime.datetime.now().strftime("%I:%M %p")
            out = "Current time is " + time
            return Response('OK', out)

        # What is the date?
        elif "date" in cmd:
            out = datetime.datetime.now().strftime("The date is %d %B %Y. It's a %A")
            return Response('OK', out)

        # Flip a coin
        elif ("flip" in cmd or "toss" in cmd) and "coin" in cmd:
            out = "I flipped a coin and got " + random.choice(('tails', 'heads'))
            return Response('OK', out)

        # Who is [person name]?
        elif "who is" in cmd:
            person = cmd.replace("who is","")
            #info = wikipedia.summary(person, 1)
            #give_output(info)
            return Response('OK', "Nobody")
        
        # What is your name?
        elif "your name" in cmd:
            possibilities = [
                f"{self.assistant.name} is the name. Helping you is the game.",
                f"My name is {self.assistant.name} and I'm your personal virtual assistant.",
                f"It's {self.assistant.name}"
            ]
            out = random.choice(possibilities)

            return Response('OK', out)

        # Tell me a joke.
        elif "joke" in cmd:
            return Response('OK', "Look in the mirror.")

        else:

            return Response('OK', "I'm sorry. I don't understand.")
