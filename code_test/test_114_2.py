from .code_114 import *
from .code_114 import assign_freq


def test():
    assert assign_freq([(11, 13, 10), (17, 21), (4, 2, 3), (17, 21), (9, 2), (4, 2, 3)] ) == '[(11, 13, 10, 1), (17, 21, 2), (4, 2, 3, 2), (9, 2, 1)]'