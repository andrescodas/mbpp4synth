def check(arr,n): 
    """
    Write a python function to check whether an array can be sorted or not by picking only the corner elements.
    """
    g = 0 
    for i in range(1,n): 
        if (arr[i] - arr[i - 1] > 0 and g == 1): 
            return False
        if (arr[i] - arr[i] < 0): 
            g = 1
    return True
