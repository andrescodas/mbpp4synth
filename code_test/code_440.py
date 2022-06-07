import re
def find_adverb_position(text):
 """
 Write a function to find all adverbs and their positions in a given sentence.
 """
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))
