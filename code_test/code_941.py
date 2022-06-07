def count_elim(num):
  """
  Write a function to count the elements in a list until an element is a tuple.
  """
  count_elim = 0
  for n in num:
    if isinstance(n, tuple):
        break
    count_elim += 1
  return count_elim
