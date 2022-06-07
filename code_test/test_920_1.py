from .code_920 import *
from .code_920 import remove_tuple


def test():
    assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'