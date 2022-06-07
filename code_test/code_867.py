def min_Num(arr,n):  
    """
    Write a python function to add a minimum number such that the sum of array becomes even.
    """
    odd = 0
    for i in range(n): 
        if (arr[i] % 2): 
            odd += 1 
    if (odd % 2): 
        return 1
    return 2
