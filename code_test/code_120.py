def max_product_tuple(list1):
    """
    Write a function to find the maximum product from the pairs of tuples within a given list.
    """
    result_max = max([abs(x * y) for x, y in list1] )
    return result_max
