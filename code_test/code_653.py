from collections import defaultdict
def grouping_dictionary(l):
    """
    Write a function to group a sequence of key-value pairs into a dictionary of lists using collections module.
    """
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d
