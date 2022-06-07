def lower_ctr(str):
      """
      Write a python function to count lower case letters in a given string.
      """
      lower_ctr= 0
      for i in range(len(str)):
          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     
      return  lower_ctr
