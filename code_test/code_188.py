def prod_Square(n):
    """
    Write a python function to check whether the given number can be represented by product of two squares or not.
    """
    for i in range(2,(n) + 1):
        if (i*i < (n+1)):
            for j in range(2,n + 1):
                if ((i*i*j*j) == n):
                    return True;
    return False;
