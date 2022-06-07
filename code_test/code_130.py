from collections import defaultdict
def max_occurrences(nums):
    """
    Write a function to find the item with maximum frequency in a given list.
    """
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result
