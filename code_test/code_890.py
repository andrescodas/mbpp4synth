def find_Extra(arr1,arr2,n) : 
    """
    Write a python function to find the index of an extra element present in one sorted array.
    """
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n 
