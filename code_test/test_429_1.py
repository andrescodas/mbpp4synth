from .code_429 import *
from .code_429 import and_tuples


def test():
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)