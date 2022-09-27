def int_suffix(i: int) -> str:
    """Returns the ordinal representation of the given number."""
    return str(i) + {1: "st", 2: "nd", 3: "rd"}.get(i % 10 * (i % 100 not in {11, 12, 13}), "th")