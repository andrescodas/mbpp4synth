def get_Odd_Occurrence(arr,arr_size):   
    """
    Write a python function to find the element occurring odd number of times.
    """
    for i in range(0,arr_size): 
        count = 0
        for j in range(0,arr_size): 
            if arr[i] == arr[j]: 
                count+=1     
        if (count % 2 != 0): 
            return arr[i]     
    return -1
