from assistant.datatypes.message import MessageTokens, Message
from assistant.utils.typecheck import is_float, is_natural_number, is_number, is_whole_number, is_integer

# todo: Not Operation

class PatternExpression:
    def __init__(self, pattern, strict=False):

        # The pattern consisting of tokens as a list.
        self.pattern = pattern

        # Whether to evaluate the expression strictly.
        # ie: making sure order is preserved.
        self.strict = strict
        
        self.tokens = self._tokenize()

    def _tokenize(self):
        """Convert the pattern into something more parsable."""
        
        tokens = []
        for token in self.pattern:
            tokens.append(self._get_token(token))
        return tokens

    def _get_token(self, string: str):
        """Get available token from string."""

        try:
            num = float(string)
            if num == 0:
                return MessageTokens.WholeNumber
            elif num == 1:
                return MessageTokens.Int
            elif num == 2:
                return MessageTokens.NaturalNumber
            elif num == 0.5:
                return MessageTokens.Float
            else:
                return MessageTokens.Number
        except:
            return string

    def match_item(self, token, msg:Message):
        """Check if an individual item of a pattern exists in a string."""
        # todo: Also return value

        if isinstance(token, str):
            return token in msg.processed
            
        elif isinstance(token, (tuple, set)):
            flag = False
            for part in token:
                if self.match_item(part, msg):
                    flag = True
                    break
            return flag
        elif token == MessageTokens.Int:
            flag = False
            for part in msg.tokenized:
                if is_integer(part):
                    flag = True
                    break
            return flag
        elif token == MessageTokens.Float:
            flag = False
            for part in msg.tokenized:
                if is_float(part):
                    flag = True
                    break
            return flag
        elif token == MessageTokens.NaturalNumber:
            flag = False
            for part in msg.tokenized:
                if is_natural_number(part):
                    flag = True
                    break
            return flag
        elif token == MessageTokens.WholeNumber:
            flag = False
            for part in msg.tokenized:
                if is_whole_number(part):
                    flag = True
                    break
            return flag
        elif token == MessageTokens.Number:
            flag = False
            for part in msg.tokenized:
                if is_number(part):
                    flag = True
                    break
            return flag

        return False

    def match(self, msg:Message):
        """Attempts to match the pattern against a Message and returns confidence"""
        passed = 0
        total = len(self.tokens)
        for ptoken in self.tokens:
            # For each part of the expression.
            matches = self.match_item(ptoken, msg)
            if matches:
                passed += 1
            else:
                # Sets are an exception
                # Because they are a "may contain" version of tuples.
                if not isinstance(ptoken, set):
                    # Instantly invalidate the entire match.
                    return 0

        return round(passed / total, 2)
    
    def match_explicit(self, msg:Message, needs:int=0.5):
        """Attempts to match the pattern against a Message and returns true/false"""
        return self.match(msg) > needs

    def extract_item(self, token, msg:Message):
        """Extract an individual item of a pattern exists in a string."""
        
        if isinstance(token, str):
            if token in msg.processed:
                return token
        elif isinstance(token, (tuple, set)):
            for part in token:
                if self.match_item(part, msg):
                    return part
        elif token == MessageTokens.Int:
            for part in msg.tokenized:
                if is_integer(part):
                    return int(part)
        elif token == MessageTokens.Float:
            for part in msg.tokenized:
                if is_float(part):
                    return float(part)
        elif token == MessageTokens.NaturalNumber:
            for part in msg.tokenized:
                if is_natural_number(part):
                    return int(part)
        elif token == MessageTokens.WholeNumber:
            for part in msg.tokenized:
                if is_whole_number(part):
                    return int(part)
        elif token == MessageTokens.Number:
            for part in msg.tokenized:
                if is_integer(part):
                    return float(part)
        return None
    
    def extract(self, msg:Message):
        """Attempts to extract values for matched tokens from the message."""
        # todo: Try to do this alongside matching
        values = {}
        for ptoken in self.tokens:
            extract = self.extract_item(ptoken, msg)
            if extract is not None:
                values[ptoken] = extract
        return values

# Alias for pattern expression.
PaExp = PatternExpression

