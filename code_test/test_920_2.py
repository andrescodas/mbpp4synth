from .code_920 import *
from .code_920 import remove_tuple


def test():
    assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'