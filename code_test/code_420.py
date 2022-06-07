def cube_Sum(n): 
    """
    Write a python function to find the cube sum of first n even natural numbers.
    """
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
