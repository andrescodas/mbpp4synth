def floor_Min(A,B,N):
    """
    Write a python function to find minimum possible value for the given periodic function.
    """
    x = max(B - 1,N)
    return (A*x) // B
