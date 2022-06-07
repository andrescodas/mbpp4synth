def remove_empty(tuple1): #L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
   """
   Write a function to remove an empty tuple from a list of tuples.
   """
   tuple1 = [t for t in tuple1 if t]
   return tuple1
