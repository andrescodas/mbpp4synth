import re
def start_withp(words):
 """
 Write a function to match two words from a list of words starting with letter 'p'.
 """
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()
