def min_length_list(input_list):
    """
    Write a function to find the list with minimum length using lambda function.
    """
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
