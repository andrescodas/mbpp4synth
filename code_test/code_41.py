def filter_evennumbers(nums):
 """
 Write a function to filter even numbers using lambda function.
 """
 even_nums = list(filter(lambda x: x%2 == 0, nums))
 return even_nums
