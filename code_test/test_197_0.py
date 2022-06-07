from .code_197 import *
from .code_197 import find_exponentio


def test():
    assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)