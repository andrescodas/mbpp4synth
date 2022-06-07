import re
def text_match_two_three(text):
        """
        Write a function that matches a string that has an a followed by two to three 'b'.
        """
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
