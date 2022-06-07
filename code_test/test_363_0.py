from .code_363 import *
from .code_363 import add_K_element


def test():
    assert add_K_element([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]