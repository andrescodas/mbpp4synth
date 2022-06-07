def sum_Of_Subarray_Prod(arr,n):
    """
    Write a python function to find sum of products of all possible subarrays.
    """
    ans = 0
    res = 0
    i = n - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
