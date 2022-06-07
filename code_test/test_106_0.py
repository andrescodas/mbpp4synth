from .code_106 import *
from .code_106 import add_lists


def test():
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)