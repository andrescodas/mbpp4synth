def check_greater(arr, number):
  """
  Write a function to check whether the entered number is greater than the elements of the given array.
  """
  arr.sort()
  if number > arr[-1]:
    return ('Yes, the entered number is greater than those in the array')
  else:
    return ('No, entered number is less than those in the array')
