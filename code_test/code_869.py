def remove_list_range(list1, leftrange, rigthrange):
   """
   Write a function to remove sublists from a given list of lists, which are outside a given range.
   """
   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]
   return result
