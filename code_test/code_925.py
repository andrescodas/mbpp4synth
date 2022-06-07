def mutiple_tuple(nums):
    """
    Write a python function to calculate the product of all the numbers of a given tuple.
    """
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product
