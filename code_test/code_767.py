def get_Pairs_Count(arr,n,sum):
    """
    Write a python function to count the number of pairs whose sum is equal to ‘sum’.
    """
    count = 0  
    for i in range(0,n):
        for j in range(i + 1,n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
