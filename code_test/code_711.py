def product_Equal(n): 
    """
    Write a python function to check whether the product of digits of a number at even and odd places is equal or not.
    """
    if n < 10: 
        return False
    prodOdd = 1; prodEven = 1
    while n > 0: 
        digit = n % 10
        prodOdd *= digit 
        n = n//10
        if n == 0: 
            break; 
        digit = n % 10
        prodEven *= digit 
        n = n//10
    if prodOdd == prodEven: 
        return True
    return False
