from .code_507 import *
from .code_507 import remove_words


def test():
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['blue', 'white'])==['red', 'green', 'black', 'orange']