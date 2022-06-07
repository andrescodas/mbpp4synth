def concatenate_tuple(test_tup):
    """
    Write a function to concatenate each element of tuple by the delimiter.
    """
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res)) 
