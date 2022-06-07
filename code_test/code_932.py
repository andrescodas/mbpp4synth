def remove_duplic_list(l):
    """
    Write a function to remove duplicate words from a given list of strings.
    """
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp
