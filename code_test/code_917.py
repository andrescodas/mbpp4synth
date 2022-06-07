import re
def text_uppercase_lowercase(text):
        """
        Write a function to find the sequences of one upper case letter followed by lower case letters.
        """
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')
