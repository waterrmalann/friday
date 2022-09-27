import time

class Response:
    """Response obtained from the engine that processed the command."""

    def __init__(self, status, content):
        # Whether the response was a success or a failure.
        # OK = Success, NOT-OK = Failure
        self.status = status
        
        # The content in the response, typically a [Message] object.
        self.content = content
        
        # A unix timestamp of when the response was obtained.
        self.timestamp = time.time()

    def __bool__(self):
        return self.status == 'OK'