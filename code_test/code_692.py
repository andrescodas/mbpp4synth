def last_Two_Digits(N): 
    """
    Write a python function to find the last two digits in factorial of a given number.
    """
    if (N >= 10): 
        return
    fac = 1
    for i in range(1,N + 1): 
        fac = (fac * i) % 100
    return (fac) 
