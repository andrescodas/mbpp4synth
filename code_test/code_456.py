def reverse_string_list(stringlist):
    """
    Write a function to reverse strings in a given list of string values.
    """
    result = [x[::-1] for x in stringlist]
    return result
