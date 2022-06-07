def count_odd(array_nums):
   """
   Write a function to find number of odd elements in the given list using lambda function.
   """
   count_odd = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
   return count_odd
