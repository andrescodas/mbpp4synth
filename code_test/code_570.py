def remove_words(list1, charlist):
    """
    Write a function to remove words from a given list of strings containing a character or string.
    """
    new_list = []
    for line in list1:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])
        new_list.append(new_words)
    return new_list
