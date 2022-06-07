def group_keyvalue(l):
    """
    Write a function to group a sequence of key-value pairs into a dictionary of lists.
    """
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
