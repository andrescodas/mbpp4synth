import math 
def count_Divisors(n) : 
    """
    Write a python function to check whether the count of divisors is even or odd.
    """
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    if (count % 2 == 0) : 
        return ("Even") 
    else : 
        return ("Odd") 
