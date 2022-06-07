from itertools import groupby
def consecutive_duplicates(nums):
    """
    Write a function to remove consecutive duplicates of a given list.
    """
    return [key for key, group in groupby(nums)] 
