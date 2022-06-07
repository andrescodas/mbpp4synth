from .code_487 import *
from .code_487 import sort_tuple


def test():
    assert sort_tuple([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]