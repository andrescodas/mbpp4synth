def maximum_product(nums):
    """
    Write a function to compute maximum product of three numbers of a given array of integers using heap queue algorithm.
    """
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
