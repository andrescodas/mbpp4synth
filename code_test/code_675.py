def sum_nums(x, y,m,n):
    """
    Write a function to add two integers. however, if the sum is between the given range it will return 20.
    """
    sum_nums= x + y
    if sum_nums in range(m, n):
        return 20
    else:
        return sum_nums
