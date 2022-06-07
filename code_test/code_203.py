def hamming_Distance(n1,n2) : 
    """
    Write a python function to find the hamming distance between given two integers.
    """
    x = n1 ^ n2  
    setBits = 0
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits  
