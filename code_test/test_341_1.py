from .code_341 import *
from .code_341 import set_to_tuple


def test():
    assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)