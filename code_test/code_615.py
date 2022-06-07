def average_tuple(nums):
    """
    Write a function to find average value of the numbers in a given tuple of tuples.
    """
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
