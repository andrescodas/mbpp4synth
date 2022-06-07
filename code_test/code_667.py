def Check_Vow(string, vowels): 
    """
    Write a python function to count number of vowels in the string.
    """
    final = [each for each in string if each in vowels] 
    return(len(final)) 
