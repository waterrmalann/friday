class IntentInterpreter:
    """Module responsible for identifying input intent and redirecting it to proper handler."""

    def __init__(self, assistant):
        
        # An instance of the assistant.
        self.assistant = assistant

        self.handlers = {}

    def attach_handler(self, handler):

        # Attach a handler to the interpreter.
        self.handlers[handler.__class__.__name__] = handler
    
    def process(self, message):
        """Takes input, processes it and handles it to the proper handler."""

        for handler in self.handlers:
            if handler.check(message):
                return handler.process(message)