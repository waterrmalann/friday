class Handler:
    def __init__(self, name):
        self.name = name
        self.interpreter = None
        self.assistant = None
        
        # If the handler is hooked to the intent interpreter and ready for use.
        self._hooked = False
        # If the handler is enabled or disabled.
        self._active = False
    
    def setup(self, interpreter):
        """Hook the interpreter and the assistant to the handler post-init."""

        # Get the instance of the intent interpreter.
        self.interpreter = interpreter
        # Get the instance of the assistant.
        self.assistant = interpreter.assistant
        # Get the instance of the logger.
        self.logger = self.assistant.logger

        self._hooked = True
    
    def is_ready(self):
        return self._hooked

    def is_active(self):
        return self._active
    
    def activate(self):
        self._active = True
    
    def deactivate(self):
        self._active = False

    def check(self):
        raise NotImplementedError
    
    def handle(self):
        raise NotImplementedError