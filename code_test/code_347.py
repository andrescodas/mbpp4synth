def count_Squares(m,n): 
    """
    Write a python function to count the number of squares in a rectangle.
    """
    if (n < m): 
        temp = m 
        m = n 
        n = temp 
    return n * (n + 1) * (3 * m - n + 1) // 6
