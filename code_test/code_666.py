def count_char(string,char):
 """
 Write a function to count occurrence of a character in a string.
 """
 count = 0
 for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
 return count
