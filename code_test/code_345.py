def diff_consecutivenums(nums):
    """
    Write a function to find the difference between two consecutive numbers in a given list.
    """
    result = [b-a for a, b in zip(nums[:-1], nums[1:])]
    return result
