def is_Product_Even(arr,n): 
    """
    Write a python function to check whether the product of numbers is even or not.
    """
    for i in range(0,n): 
        if ((arr[i] & 1) == 0): 
            return True
    return False
