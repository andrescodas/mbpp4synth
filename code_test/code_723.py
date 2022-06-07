from operator import eq
def count_same_pair(nums1, nums2):
    """
    Write a function to count the same pair in two given lists using map function.
    """
    result = sum(map(eq, nums1, nums2))
    return result
