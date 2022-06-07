def find_remainder(arr, lens, n): 
    """
    Write a python function to find remainder of array multiplication divided by n.
    """
    mul = 1
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
