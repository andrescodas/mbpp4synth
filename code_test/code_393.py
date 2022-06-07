def max_length_list(input_list):
    """
    Write a function to find the list with maximum length using lambda function.
    """
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
