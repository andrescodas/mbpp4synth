from .code_969 import *
from .code_969 import join_tuples


def test():
    assert join_tuples([(7, 8), (7, 9), (8, 10), (8, 12), (9, 15)] ) == [(7, 8, 9), (8, 10, 12), (9, 15)]