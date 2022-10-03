from assistant.handlers import Handler
from assistant.datatypes.response import Response

class Command:
    """Command Datatype"""
    # todo: if cant be tokenized, raise ValueError('could not convert string ' ' to float')

    def __init__(self, string):
        self.raw = string
        self.processed = string.strip().lower()
        self.prefix = self.processed[0]  # Prefix is assumed to be the first character.

        split = self.processed.split(' ')
        self.command_name = split[0][1:]
        self.args = split[1:]
    
    def __str__(self):
        return self.raw
    
    def __repr__(self):
        return self.command_name

class CommandHandler(Handler):
    
    def __init__(self, command: callable, aliases: tuple):
        super().__init__("Command Handler")

        # The command function that's called.
        self.command = command

        # Various names for the command.
        self.aliases = aliases + (command.__name__, )

    def handle(self, message):
        """Handle the input."""

        cmd = Command(message)
        
        try:
            ran = self.command(self.assistant, *cmd.args)
            return Response('OK', str(ran))
        except Exception as ex:
            return Response('NOT-OK', str(ex))
    
    def check(self, message):
        """Check if this is the right handler for the job."""

        #if message.strip().startswith(self.assistant.config['developer']['prefix']):

        # fixme: fix this hack job
        if message.strip()[1:].startswith(self.aliases):
            return True
        else:
            return False