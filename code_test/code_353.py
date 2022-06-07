def remove_column(list1, n):
   """
   Write a function to remove a specified column from a given nested list.
   """
   for i in list1: 
    del i[n] 
   return list1
