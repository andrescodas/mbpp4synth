import itertools
def remove_duplicate(list1):
 """
 Write a function to remove duplicates from a list of lists.
 """
 list.sort(list1)
 remove_duplicate = list(list1 for list1,_ in itertools.groupby(list1))
 return remove_duplicate
