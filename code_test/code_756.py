import re
def text_match_zero_one(text):
        """
        Write a function that matches a string that has an a followed by zero or one 'b'.
        """
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
