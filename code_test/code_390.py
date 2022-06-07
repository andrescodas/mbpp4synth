def add_string(list,string):
 """
 Write a function to insert a given string at the beginning of all items in a list.
 """
 add_string=[string.format(i) for i in  list]
 return add_string
