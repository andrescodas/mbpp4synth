def round_num(n,m):
    """
    Write a function to round the given number to the nearest multiple of a specific number.
    """
    a = (n //m) * m
    b = a + m
    return (b if n - a > b - n else a)
