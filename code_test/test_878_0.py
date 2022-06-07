from .code_878 import *
from .code_878 import check_tuples


def test():
    assert check_tuples((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True