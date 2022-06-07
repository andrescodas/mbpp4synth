def increasing_trend(nums):
    """
    Write a python function to check whether a sequence of numbers has an increasing trend or not.
    """
    if (sorted(nums)== nums):
        return True
    else:
        return False
