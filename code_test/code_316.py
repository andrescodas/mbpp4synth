def find_last_occurrence(A, x):
    """
    Write a function to find the index of the last occurrence of a given number in a sorted array.
    """
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            left = mid + 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result 
