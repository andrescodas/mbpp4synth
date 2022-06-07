def max_sum_list(lists):
 """
 Write a function to find the list in a list of lists whose sum of elements is the highest.
 """
 return max(lists, key=sum)
