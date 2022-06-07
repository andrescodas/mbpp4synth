import re
def text_match_word(text):
        """
        Write a function that matches a word at the end of a string, with optional punctuation.
        """
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'
