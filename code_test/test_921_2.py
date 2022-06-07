from .code_921 import *
from .code_921 import chunk_tuples


def test():
    assert chunk_tuples((11, 14, 16, 17, 19, 21, 22, 25), 4) == [(11, 14, 16, 17), (19, 21, 22, 25)]