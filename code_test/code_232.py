import heapq
def larg_nnum(list1,n):
 """
 Write a function to get the n largest items from a dataset.
 """
 largest=heapq.nlargest(n,list1)
 return largest
