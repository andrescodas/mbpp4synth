from .code_579 import *
from .code_579 import find_dissimilar


def test():
    assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)