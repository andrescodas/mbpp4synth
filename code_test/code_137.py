from array import array
def zero_count(nums):
    """
    Write a function to find the ration of zeroes in an array of integers.
    """
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)
