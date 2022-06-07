def sort_by_dnf(arr, n):
  """
  Write a function to sort the given array without using any sorting algorithm. the given array consists of only 0, 1, and 2.
  """
  low=0
  mid=0
  high=n-1
  while mid <= high:
    if arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      low = low + 1
      mid = mid + 1
    elif arr[mid] == 1:
      mid = mid + 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high = high - 1
  return arr
