def average_Even(n) : 
    """
    Write a python function to find the average of even numbers till a given even number.
    """
    if (n% 2!= 0) : 
        return ("Invalid Input") 
        return -1  
    sm = 0
    count = 0
    while (n>= 2) : 
        count = count+1
        sm = sm+n 
        n = n-2
    return sm // count 
