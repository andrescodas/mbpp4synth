from .code_709 import *
from .code_709 import get_unique


def test():
    assert get_unique([(4, 5), (2, 3), (3, 5), (9, 3), (8, 3), (9, 2), (10, 2), (9, 5), (11, 5)] ) == '{5: 4, 3: 3, 2: 2}'