def gcd(p,q):
    while q != 0:
        p, q = q,p%q
    return p
def is_coprime(x,y):
    """
    Write a python function to check whether the given number is co-prime or not.
    """
    return gcd(x,y) == 1
