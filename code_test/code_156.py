def tuple_int_str(tuple_str):
    """
    Write a function to convert a tuple of string values to a tuple of integer values.
    """
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
