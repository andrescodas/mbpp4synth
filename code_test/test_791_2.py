from .code_791 import *
from .code_791 import remove_nested


def test():
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)