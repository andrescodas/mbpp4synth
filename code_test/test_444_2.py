from .code_444 import *
from .code_444 import trim_tuple


def test():
    assert trim_tuple([(7, 8, 4, 9), (11, 8, 12, 4),(4, 1, 7, 8), (3, 6, 9, 7)], 1) == '[(8, 4), (8, 12), (1, 7), (6, 9)]'