from .code_612 import *
from .code_612 import merge


def test():
    assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]