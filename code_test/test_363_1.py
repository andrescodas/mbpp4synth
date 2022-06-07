from .code_363 import *
from .code_363 import add_K_element


def test():
    assert add_K_element([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8) == [(9, 10, 11), (12, 13, 14), (15, 16, 17)]