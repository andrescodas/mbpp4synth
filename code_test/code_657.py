import math 
def first_Digit(n) : 
    """
    Write a python function to find the first digit in factorial of a given number.
    """
    fact = 1
    for i in range(2,n + 1) : 
        fact = fact * i 
        while (fact % 10 == 0) :  
            fact = int(fact / 10) 
    while (fact >= 10) : 
        fact = int(fact / 10) 
    return math.floor(fact) 
