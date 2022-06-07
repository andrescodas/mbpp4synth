def is_Perfect_Square(n) :
    """
    Write a python function to check whether the given number is a perfect square or not.
    """
    i = 1
    while (i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True     
        i = i + 1
    return False
