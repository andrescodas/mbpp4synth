def frequency_Of_Largest(n,arr): 
    """
    Write a python function to find the frequency of the largest value in a given array.
    """
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] >mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq 
