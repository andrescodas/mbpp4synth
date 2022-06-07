def frequency(a,x): 
    """
    Write a python function to find the frequency of a number in a given array.
    """
    count = 0  
    for i in a: 
        if i == x: count += 1
    return count 
