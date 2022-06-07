def re_order(A):
    """
    Write a function to move all zeroes to the end of the given array.
    """
    k = 0
    for i in A:
        if i:
            A[k] = i
            k = k + 1
    for i in range(k, len(A)):
        A[i] = 0
    return A
