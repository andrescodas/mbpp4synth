def even_Power_Sum(n): 
    """
    Write a python function to find the sum of fourth power of first n even natural numbers.
    """
    sum = 0; 
    for i in range(1,n + 1): 
        j = 2*i; 
        sum = sum + (j*j*j*j); 
    return sum; 
