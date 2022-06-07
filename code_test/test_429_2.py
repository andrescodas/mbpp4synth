from .code_429 import *
from .code_429 import and_tuples


def test():
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)