from collections import Counter 
def max_char(str1):
    """
    Write a function to count the most common character in a given string.
    """
    temp = Counter(str1) 
    max_char = max(temp, key = temp.get)
    return max_char
