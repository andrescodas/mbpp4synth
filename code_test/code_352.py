def unique_Characters(str):
    """
    Write a python function to check whether all the characters in a given string are unique.
    """
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if (str[i] == str[j]):
                return False;
    return True;
