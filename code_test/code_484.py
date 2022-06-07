def remove_matching_tuple(test_list1, test_list2):
  """
  Write a function to remove the matching tuples from the given two tuples.
  """
  res = [sub for sub in test_list1 if sub not in test_list2]
  return (res) 
