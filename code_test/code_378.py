def move_first(test_list):
  """
  Write a python function to shift last element to first position in the given list.
  """
  test_list = test_list[-1:] + test_list[:-1]  
  return test_list
