def capitalize_first_last_letters(str1):
     """
     Write a python function to capitalize first and last letters of each word of a given string.
     """
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
