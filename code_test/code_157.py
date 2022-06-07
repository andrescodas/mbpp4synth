from itertools import groupby
def encode_list(list1):
    """
    Write a function to reflect the run-length encoding from a list.
    """
    return [[len(list(group)), key] for key, group in groupby(list1)]
