from .code_505 import *
from .code_505 import re_order


def test():
    assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]