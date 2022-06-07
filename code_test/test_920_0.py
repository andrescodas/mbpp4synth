from .code_920 import *
from .code_920 import remove_tuple


def test():
    assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'