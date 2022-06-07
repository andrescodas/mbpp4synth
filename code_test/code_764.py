def number_ctr(str):
      """
      Write a python function to count numeric values in a given string.
      """
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
