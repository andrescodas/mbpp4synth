def first_Factorial_Divisible_Number(x): 
    """
    Write a python function to find the first natural number whose factorial is divisible by x.
    """
    i = 1;
    fact = 1; 
    for i in range(1,x): 
        fact = fact * i 
        if (fact % x == 0): 
            break
    return i 
