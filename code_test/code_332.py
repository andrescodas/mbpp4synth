def char_frequency(str1):
    """
    Write a function to count character frequency of a given string.
    """
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
