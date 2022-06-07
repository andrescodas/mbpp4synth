import re
def remove_parenthesis(items):
 """
 Write a function to remove the parenthesis area in a string.
 """
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))
