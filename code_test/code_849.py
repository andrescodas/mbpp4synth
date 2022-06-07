def Sum(N): 
    """
    Write a python function to find sum of all prime divisors of a given number.
    """
    SumOfPrimeDivisors = [0]*(N + 1)   
    for i in range(2,N + 1) : 
        if (SumOfPrimeDivisors[i] == 0) : 
            for j in range(i,N + 1,i) : 
                SumOfPrimeDivisors[j] += i           
    return SumOfPrimeDivisors[N] 
