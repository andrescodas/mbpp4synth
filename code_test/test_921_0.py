from .code_921 import *
from .code_921 import chunk_tuples


def test():
    assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]