from collections import Counter 
def count_Occurrence(tup, lst): 
    """
    Write a python function to count the occurence of all elements of list in a tuple.
    """
    count = 0
    for item in tup: 
        if item in lst: 
            count+= 1 
    return count  
