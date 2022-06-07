def count_char_position(str1): 
    """
    Write a python function to count characters at same position in a given string (lower and uppercase characters) as in english alphabet.
    """
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
