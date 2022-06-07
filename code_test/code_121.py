def check_triplet(A, n, sum, count):
    """
    Write a function to find the triplet with sum of the given array
    """
    if count == 3 and sum == 0:
        return True
    if count == 3 or n == 0 or sum < 0:
        return False
    return check_triplet(A, n - 1, sum - A[n - 1], count + 1) or\
           check_triplet(A, n - 1, sum, count)
