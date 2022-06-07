from .code_570 import *
from .code_570 import remove_words


def test():
    assert remove_words(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['&', '+', '@'])==['Red', '', 'Green', 'Orange', 'White']