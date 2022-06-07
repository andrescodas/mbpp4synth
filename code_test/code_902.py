from collections import Counter
def add_dict(d1,d2):
   """
   Write a function to combine two dictionaries by adding values for common keys.
   """
   add_dict = Counter(d1) + Counter(d2)
   return add_dict
