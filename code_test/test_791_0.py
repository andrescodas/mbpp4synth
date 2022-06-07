from .code_791 import *
from .code_791 import remove_nested


def test():
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)