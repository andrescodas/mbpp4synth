from .code_709 import *
from .code_709 import get_unique


def test():
    assert get_unique([(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)] ) == '{4: 4, 2: 3, 1: 2}'