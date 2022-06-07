from .code_193 import *
from .code_193 import remove_tuple


def test():
    assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)