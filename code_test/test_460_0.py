from .code_460 import *
from .code_460 import Extract


def test():
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]