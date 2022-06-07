from .code_196 import *
from .code_196 import remove_tuples


def test():
    assert remove_tuples([(4, 5), (4,5), (6, 7), (1, 2, 3), (3, 4, 6, 7)] ,2) == [(1, 2, 3), (3, 4, 6, 7)]