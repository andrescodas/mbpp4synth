import re
def text_match_one(text):
        """
        Write a function that matches a string that has an a followed by one or more b's.
        """
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
