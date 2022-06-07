from .code_893 import *
from .code_893 import Extract


def test():
    assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]