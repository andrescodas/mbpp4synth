from .code_429 import *
from .code_429 import and_tuples


def test():
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)