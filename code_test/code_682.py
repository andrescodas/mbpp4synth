def mul_list(nums1,nums2):
  """
  Write a function to multiply two lists using map and lambda function.
  """
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)
