def count_even(array_nums):
   """
   Write a function to find number of even elements in the given list using lambda function.
   """
   count_even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
   return count_even
