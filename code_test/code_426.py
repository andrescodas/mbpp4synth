def filter_oddnumbers(nums):
 """
 Write a function to filter odd numbers using lambda function.
 """
 odd_nums = list(filter(lambda x: x%2 != 0, nums))
 return odd_nums
