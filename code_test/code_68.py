def is_Monotonic(A): 
    """
    Write a python function to check whether the given array is monotonic or not.
    """
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
