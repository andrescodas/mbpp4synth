def count_X(tup, x): 
    """
    Write a python function to count the occcurences of an element in a tuple.
    """
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count 
