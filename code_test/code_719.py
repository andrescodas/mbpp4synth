import re
def text_match(text):
        """
        Write a function that matches a string that has an a followed by zero or more b's.
        """
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
