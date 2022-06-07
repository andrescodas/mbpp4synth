import re
def text_match_wordz_middle(text):
        """
        Write a function that matches a word containing 'z', not at the start or end of the word.
        """
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
