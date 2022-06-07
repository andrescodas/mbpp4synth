def decode_list(alist):
    """
    Write a function to decode a run-length encoded given list.
    """
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]
