import re
def text_match_string(text):
        """
        Write a function that matches a word at the beginning of a string.
        """
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'
