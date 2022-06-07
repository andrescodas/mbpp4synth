from .code_505 import *
from .code_505 import re_order


def test():
    assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]