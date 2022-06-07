import re
def text_starta_endb(text):
        """
        Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
        """
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
