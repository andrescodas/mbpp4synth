def find_Odd_Pair(A,N) : 
    """
    Write a python function to count the pairs with xor as an odd number.
    """
    oddPair = 0
    for i in range(0,N) :  
        for j in range(i+1,N) :  
            if ((A[i] ^ A[j]) % 2 != 0):  
                oddPair+=1  
    return oddPair  
