def sum_Of_Series(n): 
    """
    Write a python function to find the cube sum of first n natural numbers.
    """
    sum = 0
    for i in range(1,n + 1): 
        sum += i * i*i       
    return sum
