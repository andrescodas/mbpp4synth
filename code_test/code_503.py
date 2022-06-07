def add_consecutive_nums(nums):
    """
    Write a function to add consecutive numbers of a given list.
    """
    result = [b+a for a, b in zip(nums[:-1], nums[1:])]
    return result
