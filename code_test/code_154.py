def specified_element(nums, N):
    """
    Write a function to extract every specified element from a given two dimensional list.
    """
    result = [i[N] for i in nums]
    return result
