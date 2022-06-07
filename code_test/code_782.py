def Odd_Length_Sum(arr):
    """
    Write a python function to find the sum of all odd length subarrays.
    """
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
