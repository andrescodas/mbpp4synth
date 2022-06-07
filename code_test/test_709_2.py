from .code_709 import *
from .code_709 import get_unique


def test():
    assert get_unique([(6, 5), (3, 4), (2, 6), (11, 1), (8, 22), (8, 11), (4, 3), (14, 3), (11, 6)] ) == '{5: 1, 4: 1, 6: 2, 1: 1, 22: 1, 11: 1, 3: 2}'