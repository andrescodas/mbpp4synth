def count_Squares(m,n):
    """
    Write a python function to count the number of squares in a rectangle.
    """
    if(n < m):
        temp = m
        m = n
        n = temp
    return ((m * (m + 1) * (2 * m + 1) / 6 + (n - m) * m * (m + 1) / 2))
