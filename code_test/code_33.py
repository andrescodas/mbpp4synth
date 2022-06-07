def decimal_To_Binary(N): 
    """
    Write a python function to convert a decimal number to binary number.
    """
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10,cnt)  
        B_Number += rem*c  
        N //= 2 
        cnt += 1
    return B_Number  
