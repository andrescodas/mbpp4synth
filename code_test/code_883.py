def div_of_nums(nums,m,n):
 """
 Write a function to find numbers divisible by m and n from a list of numbers using lambda function.
 """
 result = list(filter(lambda x: (x % m == 0 and x % n == 0), nums)) 
 return result
