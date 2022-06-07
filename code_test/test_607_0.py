from .code_607 import *
from .code_607 import find_literals


def test():
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)