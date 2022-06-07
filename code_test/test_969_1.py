from .code_969 import *
from .code_969 import join_tuples


def test():
    assert join_tuples([(6, 7), (6, 8), (7, 9), (7, 11), (8, 14)] ) == [(6, 7, 8), (7, 9, 11), (8, 14)]