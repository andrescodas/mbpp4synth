def get_pairs_count(arr, n, sum):
    """
    Write a function to find all pairs in an integer array whose sum is equal to a given number.
    """
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
