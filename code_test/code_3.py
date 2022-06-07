import math
def is_not_prime(n):
    """
    Write a python function to identify non-prime numbers.
    """
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
