def find_Min_Diff(arr,n): 
    """
    Write a python function to find the minimum difference between any two elements in a given array.
    """
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
