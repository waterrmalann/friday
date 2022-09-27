def is_natural_number(string):
    """Check if string is a natural number."""
    if string.strip().isdigit():
        return int(string) > 0
    return False

def is_whole_number(string):
    """Check if string is a whole number."""
    if string.strip().isdigit():
        return int(string) >= 0
    return False

def is_integer(string):
    """Check if string is integer."""
    try:
        parsed = float(string)
        return parsed == int(parsed)
    except ValueError:
        pass
    return False

def is_float(string):
    """Check if string is decimal number."""
    try:
        parsed = float(string)
        return parsed != int(parsed)
    except ValueError:
        pass
    return False

def is_number(string):
    """Check if string is any kind of number."""
    try:
        parsed = float(string)
        return True
    except ValueError:
        pass
    return False