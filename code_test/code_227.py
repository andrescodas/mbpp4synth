def min_of_three(a,b,c): 
      """
      Write a function to find minimum of three numbers.
      """
      if (a <= b) and (a <= c): 
        smallest = a 
      elif (b <= a) and (b <= c): 
        smallest = b 
      else: 
        smallest = c 
      return smallest 
