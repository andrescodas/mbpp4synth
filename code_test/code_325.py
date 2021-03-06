def get_Min_Squares(n):
    """
    Write a python function to find the minimum number of squares whose sum is equal to a given number.
    """
    if n <= 3:
        return n;
    res = n 
    for x in range(1,n + 1):
        temp = x * x;
        if temp > n:
            break
        else:
            res = min(res,1 + get_Min_Squares(n  - temp)) 
    return res;
