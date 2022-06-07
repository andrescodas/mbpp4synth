def zip_list(list1,list2):  
 """
 Write a function to zip two given lists of lists.
 """
 result = list(map(list.__add__, list1, list2)) 
 return result
