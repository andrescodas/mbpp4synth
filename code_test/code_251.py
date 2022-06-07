def insert_element(list,element):
 """
 Write a function to insert an element before each element of a list.
 """
 list = [v for elt in list for v in (element, elt)]
 return list
