def sum_Natural(n): 
    sum = (n * (n + 1)) 
    return int(sum) 
def sum_Even(l,r): 
    """
    Write a python function to find the sum of all even natural numbers within the range l and r.
    """
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2))) 
