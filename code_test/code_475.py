from collections import Counter
def sort_counter(dict1):
 """
 Write a function to sort counter by value.
 """
 x = Counter(dict1)
 sort_counter=x.most_common()
 return sort_counter
