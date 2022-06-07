import math  
def fourth_Power_Sum(n): 
    """
    Write a python function to find the sum of fourth power of n natural numbers.
    """
    sum = 0
    for i in range(1,n+1) : 
        sum = sum + (i*i*i*i) 
    return sum
