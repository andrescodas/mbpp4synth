import re
def num_position(text):
 """
 Write a function to separate and print the numbers and their position of a given string.
 """
 for m in re.finditer("\d+", text):
    return m.start()
