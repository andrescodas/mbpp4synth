def long_words(n, str):
    """
    Write a function to shortlist words that are longer than n from a given list of words.
    """
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
