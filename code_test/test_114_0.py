from .code_114 import *
from .code_114 import assign_freq


def test():
    assert assign_freq([(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)] ) == '[(6, 5, 8, 3), (2, 7, 2), (9, 1)]'