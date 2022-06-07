import re  
def remove(list): 
    """
    Write a python function to remove all digits from a list of strings.
    """
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list
