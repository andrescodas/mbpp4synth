import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    """
    Write a function to merge three dictionaries into a single expression.
    """
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict
