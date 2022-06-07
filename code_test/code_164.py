import math 
def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +math.floor(n / i)); 
        i += 1; 
    return sum; 
def areEquivalent(num1,num2): 
    """
    Write a python function to check whether the sum of divisors are same or not.
    """
    return divSum(num1) == divSum(num2); 
