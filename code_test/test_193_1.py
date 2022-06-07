from .code_193 import *
from .code_193 import remove_tuple


def test():
    assert remove_tuple((2, 3, 4, 4, 5, 6, 6, 7, 8, 8)) == (2, 3, 4, 5, 6, 7, 8)