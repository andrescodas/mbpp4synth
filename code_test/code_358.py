def moddiv_list(nums1,nums2):
  """
  Write a function to find modulo division of two lists using map and lambda function.
  """
  result = map(lambda x, y: x % y, nums1, nums2)
  return list(result)
