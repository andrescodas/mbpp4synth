from .code_487 import *
from .code_487 import sort_tuple


def test():
    assert sort_tuple([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]