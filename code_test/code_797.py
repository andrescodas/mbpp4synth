def sum_Odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_Range(l,r): 
    """
    Write a python function to find the sum of all odd natural numbers within the range l and r.
    """
    return sum_Odd(r) - sum_Odd(l - 1)
