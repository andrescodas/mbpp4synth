from .code_470 import *
from .code_470 import add_pairwise


def test():
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)