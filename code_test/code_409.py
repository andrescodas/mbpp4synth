def min_product_tuple(list1):
    """
    Write a function to find the minimum product from the pairs of tuples within a given list.
    """
    result_min = min([abs(x * y) for x, y in list1] )
    return result_min
