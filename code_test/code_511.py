def find_Min_Sum(num): 
    """
    Write a python function to find minimum sum of factors of a given number.
    """
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum
