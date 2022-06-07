from .code_570 import *
from .code_570 import remove_words


def test():
    assert remove_words(['Red color', 'Orange#', 'Green', 'Orange @', "White"],['#', 'color', '@'])==['Red', '', 'Green', 'Orange', 'White']