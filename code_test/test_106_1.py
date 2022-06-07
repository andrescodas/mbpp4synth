from .code_106 import *
from .code_106 import add_lists


def test():
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)