def sort_dict_item(test_dict):
  """
  Write a function to sort dictionary items by tuple product of keys for the given dictionary with tuple keys.
  """
  res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[1] * ele[0])}
  return  (res) 
