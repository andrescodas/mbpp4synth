def pair_OR_Sum(arr,n) : 
    """
    Write a python function to find the sum of xor of all pairs of numbers in the given array.
    """
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
