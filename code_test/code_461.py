def upper_ctr(str):
    """
    Write a python function to count the upper case characters in a given string.
    """
    upper_ctr = 0
    for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          return upper_ctr
