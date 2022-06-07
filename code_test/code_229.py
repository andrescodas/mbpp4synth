def re_arrange_array(arr, n):
  """
  Write a function to re-arrange the elements of the given array so that all negative elements appear before positive ones.
  """
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
