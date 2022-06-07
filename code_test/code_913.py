import re
def end_num(string):
    """
    Write a function to check for a number at the end of a string.
    """
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
