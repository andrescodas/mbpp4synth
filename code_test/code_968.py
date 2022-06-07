def floor_Max(A,B,N):
    """
    Write a python function to find maximum possible value for the given periodic function.
    """
    x = min(B - 1,N)
    return (A*x) // B
