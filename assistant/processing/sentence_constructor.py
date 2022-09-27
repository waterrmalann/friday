import random

"""
    ('heads', 'tails') -> randomly pick one element
        ('name is', '') -> randomly pick one element or not at all [todo: best if you can set weights]
"""

# todo
# dont add space before , . etc...
# "hello", (', world', ', you') should not be "hello , you" or "hello , world". It should be "hello, world" or "hello, you"

class SentenceConstructor:
    def __init__(self, syntaxes=None):
        self.syntaxes = syntaxes or []
        self.permutations = 0
    
    def calculate_permutations(self):
        permutations = 0
        for syntax in self.syntaxes:
            possibilities = len(syntax[0])
            for i in range(1, len(syntax)):
                possibilities *= len(syntax[i])
            permutations += possibilities
        return permutations
    
    def add_syntax(self, syntax):
        self.syntaxes.append(syntax)
        self.permutations = self.calculate_permutations()
    
    def generate(self, *args, **kwargs):
        """Generate a sentence using any available sentence expression."""
        
        # Randomly select an available SentExp to use.
        syntax = random.choice(self.syntaxes)
        # Constructed message
        constructed = []
        
        for token in syntax:
            if isinstance(token, (str, int)):
                # eg: "hello" or 12 -> append as is
                constructed.append(str(token))
            elif isinstance(token, tuple):
                # eg: ('heads', 'tails') -> randomly pick one element
                constructed.append(random.choice(token))
            elif isinstance(token, set):
                # eg: {'is', } -> randomly pick an element or not at all
                if random.random() > 0.5:
                    constructed.append(random.choice(list(token)))
            else:
                constructed.append(str(token))
                # raise InvalidSentenceToken

        joined = ' '.join(constructed)  # join list into a string
        if args:
            joined = joined.format(*args)  # format string with the params
        if kwargs:
            joined = joined.format(**kwargs)
        return joined.strip()