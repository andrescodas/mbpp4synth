from .code_878 import *
from .code_878 import check_tuples


def test():
    assert check_tuples((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False