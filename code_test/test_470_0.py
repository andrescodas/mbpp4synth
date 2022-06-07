from .code_470 import *
from .code_470 import add_pairwise


def test():
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)