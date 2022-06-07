def ntimes_list(nums,n):
    """
    Write a function to print n-times a list using map function.
    """
    result = map(lambda x:n*x, nums) 
    return list(result)
