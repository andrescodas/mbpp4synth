def get_odd_occurence(arr, arr_size):
  """
  Write a function to find the number which occurs for odd number of times in the given array.
  """
  for i in range(0, arr_size):
    count = 0
    for j in range(0, arr_size):
      if arr[i] == arr[j]:
        count += 1
    if (count % 2 != 0):
      return arr[i]
  return -1
