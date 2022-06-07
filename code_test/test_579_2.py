from .code_579 import *
from .code_579 import find_dissimilar


def test():
    assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)