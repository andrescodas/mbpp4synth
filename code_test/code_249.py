def intersection_array(array_nums1,array_nums2):
 """
 Write a function to find the intersection of two arrays using lambda function.
 """
 result = list(filter(lambda x: x in array_nums1, array_nums2)) 
 return result
