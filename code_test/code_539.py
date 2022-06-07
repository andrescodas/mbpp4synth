def basesnum_coresspondingnum(bases_num,index):
  """
  Write a function to create a list containing the power of said number in bases raised to the corresponding number in the index using map function.
  """
  result = list(map(pow, bases_num, index))
  return result
