from .code_969 import *
from .code_969 import join_tuples


def test():
    assert join_tuples([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] ) == [(5, 6, 7), (6, 8, 10), (7, 13)]