def count_Pairs(arr,n): 
    """
    Write a python function to count unequal element pairs from the given array.
    """
    cnt = 0; 
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] != arr[j]): 
                cnt += 1; 
    return cnt; 
