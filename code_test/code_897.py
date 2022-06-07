def is_Word_Present(sentence,word): 
    """
    Write a python function to check whether the word is present in a given sentence or not.
    """
    s = sentence.split(" ") 
    for i in s:  
        if (i == word): 
            return True
    return False
