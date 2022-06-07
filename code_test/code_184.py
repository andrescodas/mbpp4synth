def greater_specificnum(list,num):
 """
 Write a function to find all the values in a list that are greater than a specified number.
 """
 greater_specificnum=all(x >= num for x in list)
 return greater_specificnum
