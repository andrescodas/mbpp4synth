import re
def text_match_wordz(text):
        """
        Write a function that matches a word containing 'z'.
        """
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
