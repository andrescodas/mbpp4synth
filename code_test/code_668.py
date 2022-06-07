import re 
def replace(string, char): 
    """
    Write a python function to replace multiple occurence of character by single.
    """
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string 
