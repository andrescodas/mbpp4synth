from .code_505 import *
from .code_505 import re_order


def test():
    assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]