def min_length(list1):
   """
   Write a function to find the list of lists with minimum length.
   """
   min_length = min(len(x) for x in  list1 )  
   min_list = min((x) for x in   list1)
   return(min_length, min_list)     
