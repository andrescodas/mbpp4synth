def list_split(S, step):
    """
    Write a function to split a list for every nth element.
    """
    return [S[i::step] for i in range(step)]
