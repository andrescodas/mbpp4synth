from .code_438 import *
from .code_438 import count_bidirectional


def test():
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '2'