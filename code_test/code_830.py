import math
def round_up(a, digits):
    """
    Write a function to round up a number to specific digits.
    """
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)
