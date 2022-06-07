def difference(n) :  
    """
    Write a python function to find the difference between sum of cubes of first n natural numbers and the sum of first n natural numbers.
    """
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;  
