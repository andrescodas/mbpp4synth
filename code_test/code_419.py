def round_and_sum(list1):
  """
  Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
  """
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum
