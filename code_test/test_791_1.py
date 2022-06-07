from .code_791 import *
from .code_791 import remove_nested


def test():
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)