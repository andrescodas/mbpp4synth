def tuple_to_int(nums):
    """
    Write a function to convert a given tuple of positive integers into an integer.
    """
    result = int(''.join(map(str,nums)))
    return result
