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

class CommandHandler:
    
    def __init__(self, interpreter, config):
        
        # Contains only the prefix for now.
        self.config = config
        
        # Get the instance of the intent interpreter.
        self.interpreter = interpreter

        # Get the instance of the assistant.
        self.assistant = interpreter.assistant

        # Get the instance of the logger.
        self.logger = self.assistant.logger

        # Commands available to the command handler.
        self.commands = []
    
    def register_command(self, command, aliases):
        """Register a command with the handler."""

        self.commands.append((command, aliases))

    def unregister_command(self, command):
        """Unregister a command from the handler by command name, aliases, or function."""

        indx = None
        for i, cmd in enumerate(self.commands):
            if (command == cmd[0].__name__) or (command == cmd[0]) or (command in cmd[1]):
                indx = i
                break
        if indx is not None:
            self.commands.pop(indx)
        else:
            pass
            # raise CommandHandlerError('command is not registered')

    def handle(self, message):
        command = Command(message)

        for i, cmd in enumerate(self.commands):
            if (command.command_name == cmd[0].__name__) or (command.command_name in cmd[1]):
                return cmd[0](*command.args)  # call the command using the arguments
        else:
            return Response('NOT-OK', "Unknown Command")
    
    def check(self, message):
        if message.strip().startswith(self.assistant.config['developer']['prefix']):
            return True
        else:
            return False