from .code_114 import *
from .code_114 import assign_freq


def test():
    assert assign_freq([(4, 2, 4), (7, 1), (4, 8), (4, 2, 4), (9, 2), (7, 1)] ) == '[(4, 2, 4, 2), (7, 1, 2), (4, 8, 1), (9, 2, 1)]'