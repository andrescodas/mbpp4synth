from .code_878 import *
from .code_878 import check_tuples


def test():
    assert check_tuples((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True