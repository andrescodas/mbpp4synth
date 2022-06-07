def square_nums(nums):
 """
 Write a function to find squares of individual elements in a list using lambda function.
 """
 square_nums = list(map(lambda x: x ** 2, nums))
 return square_nums
