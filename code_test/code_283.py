def validate(n): 
    """
    Write a python function to check whether the frequency of each digit is less than or equal to the digit itself.
    """
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
