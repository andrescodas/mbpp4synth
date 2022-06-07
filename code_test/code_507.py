def remove_words(list1, removewords):
    """
    Write a function to remove specific words from a given list.
    """
    for word in list(list1):
        if word in removewords:
            list1.remove(word)
    return list1  
