def check_Concat(str1,str2):
    """
    Write a python function to check if the string is a concatenation of another string.
    """
    N = len(str1)
    M = len(str2)
    if (N % M != 0):
        return False
    for i in range(N):
        if (str1[i] != str2[i % M]):
            return False         
    return True
