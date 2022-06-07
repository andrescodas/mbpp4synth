from .code_81 import *
from .code_81 import zip_tuples


def test():
    assert zip_tuples((8, 9, 5, 6, 10, 11),(2, 6, 7) ) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]