def divisible_by_digits(startnum, endnum):
    """
    Write a function to find numbers within a given range where every number is divisible by every digit it contains.
    """
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
