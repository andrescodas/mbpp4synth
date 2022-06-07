from .code_81 import *
from .code_81 import zip_tuples


def test():
    assert zip_tuples((7, 8, 4, 5, 9, 10),(1, 5, 6) ) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]