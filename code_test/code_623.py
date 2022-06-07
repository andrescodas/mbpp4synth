def nth_nums(nums,n):
 """
 Write a function to find the n-th power of individual elements in a list using lambda function.
 """
 nth_nums = list(map(lambda x: x ** n, nums))
 return nth_nums
