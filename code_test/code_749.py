def sort_numeric_strings(nums_str):
    """
    Write a function to sort a given list of strings of numbers numerically.
    """
    result = [int(x) for x in nums_str]
    result.sort()
    return result
