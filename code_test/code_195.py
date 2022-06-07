def first(arr,x,n): 
    """
    Write a python function to find the first position of an element in a sorted array.
    """
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res
