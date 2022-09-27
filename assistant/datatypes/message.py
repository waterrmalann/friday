import enum

class MessageTokens(enum.Enum):
    Int = 0 # both negative and positive integers
    Float = 1 # both negative and positive floats / rationals
    String = 2 # any kind of string
    
    NaturalNumber = 4 # natural numbers 1 - infinity
    WholeNumber = 5 # whole numbers 0 - infinity
    Number = 6  # any integer or float

# actual input from USER
class Message:
    def __init__(self, string):
        self.raw = string
        self.processed = string.strip().lower()
        self.tokenized = self._tokenize()
    
    def _tokenize(self):
        split = self.processed.split(' ')
        tokens = []
        for token in split:
            if isinstance(token, MessageTokens):
                # a message token
                tokens.append(token)
            elif isinstance(token, tuple):
                tokens.append(token)
            elif isinstance(token, str):
                pass
        return split
    
    def __str__(self):
        return self.raw
    
    def __repr__(self):
        return self.tokenized