from .code_470 import *
from .code_470 import add_pairwise


def test():
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)