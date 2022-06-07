def tuple_intersection(test_list1, test_list2):
  """
  Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
  """
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
