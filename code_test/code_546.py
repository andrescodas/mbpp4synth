def last_occurence_char(string,char):
 """
 Write a function to find the last occurrence of a character in a string.
 """
 flag = -1
 for i in range(len(string)):
     if(string[i] == char):
         flag = i
 if(flag == -1):
    return None
 else:
    return flag + 1
