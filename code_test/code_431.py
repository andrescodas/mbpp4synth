def common_element(list1, list2):
     """
     Write a function that takes two lists and returns true if they have at least one common element.
     """
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
