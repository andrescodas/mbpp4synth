def word_len(s): 
    """
    Write a python function to check whether the length of the word is even or not.
    """
    s = s.split(' ')   
    for word in s:    
        if len(word)%2==0: 
            return True  
        else:
          return False
