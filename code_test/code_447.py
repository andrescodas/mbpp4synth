def cube_nums(nums):
 """
 Write a function to find cubes of individual elements in a list using lambda function.
 """
 cube_nums = list(map(lambda x: x ** 3, nums))
 return cube_nums
