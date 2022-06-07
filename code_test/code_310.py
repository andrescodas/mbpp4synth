def string_to_tuple(str1):
    """
    Write a function to convert a given string to a tuple.
    """
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
