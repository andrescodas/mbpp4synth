def count_Rotation(arr,n):   
    """
    Write a python function to count the number of rotations required to generate a sorted array.
    """
    for i in range (1,n): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
