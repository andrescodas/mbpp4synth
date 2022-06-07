def sum_Pairs(arr,n): 
    """
    Write a python function to find the sum of absolute differences in all pairs of the given array.
    """
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum
