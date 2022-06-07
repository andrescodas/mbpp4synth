def dict_filter(dict,n):
 """
 Write a function to filter a dictionary based on values.
 """
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result
