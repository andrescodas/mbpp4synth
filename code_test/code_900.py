import re
def match_num(string):
    """
    Write a function where a string will start with a specific number.
    """
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
