def string_list_to_tuple(str1):
    """
    Write a python function to convert a given string list to a tuple.
    """
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
