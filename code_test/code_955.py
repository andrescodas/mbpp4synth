def is_abundant(n):
    """
    Write a function to find out, if the given number is abundant.
    """
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctrsum > n
