from .code_921 import *
from .code_921 import chunk_tuples


def test():
    assert chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 2) == [(1, 2), (3, 4), (5, 6), (7, 8), (9,)]