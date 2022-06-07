def dict_depth(d):
    """
    Write a function to find the depth of a dictionary.
    """
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
