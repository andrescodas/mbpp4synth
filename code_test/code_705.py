def sort_sublists(list1):
      """
      Write a function to sort a list of lists by length and value.
      """
      list1.sort()  
      list1.sort(key=len)
      return  list1
