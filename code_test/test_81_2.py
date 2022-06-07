from .code_81 import *
from .code_81 import zip_tuples


def test():
    assert zip_tuples((9, 10, 6, 7, 11, 12),(3, 7, 8) ) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]