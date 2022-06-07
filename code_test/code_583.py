def catalan_number(num):
    """
    Write a function for nth catalan number.
    """
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
