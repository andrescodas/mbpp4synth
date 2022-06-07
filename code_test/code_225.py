def find_Min(arr,low,high): 
    """
    Write a python function to find the minimum element in a sorted and rotated array.
    """
    while (low < high): 
        mid = low + (high - low) // 2;   
        if (arr[mid] == arr[high]): 
            high -= 1; 
        elif (arr[mid] > arr[high]): 
            low = mid + 1; 
        else: 
            high = mid; 
    return arr[high]; 
