def extract_column(list1, n):
   """
   Write a function to extract a specified column from a given nested list.
   """
   result = [i.pop(n) for i in list1]
   return result 
