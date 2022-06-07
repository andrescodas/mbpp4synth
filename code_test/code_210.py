import re
def is_allowed_specific_char(string):
    """
    Write a function to check that the given string contains only a certain set of characters(in this case a-z, a-z and 0-9) by using regex.
    """
    get_char = re.compile(r'[^a-zA-Z0-9.]')
    string = get_char.search(string)
    return not bool(string)
