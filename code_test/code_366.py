def adjacent_num_product(list_nums):
    """
    Write a python function to find the largest product of the pair of adjacent elements from a given list of integers.
    """
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))
