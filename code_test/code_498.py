def gcd(x, y):
    """
    Write a python function to find gcd of two positive integers.
    """
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd
