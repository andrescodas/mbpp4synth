from .code_579 import *
from .code_579 import find_dissimilar


def test():
    assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)