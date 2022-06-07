def cube_Sum(n): 
    """
    Write a python function to find the cube sum of first n odd natural numbers.
    """
    sum = 0   
    for i in range(0,n) : 
        sum += (2*i+1)*(2*i+1)*(2*i+1) 
    return sum
