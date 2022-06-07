from .code_106 import *
from .code_106 import add_lists


def test():
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)