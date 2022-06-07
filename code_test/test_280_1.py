from .code_280 import *
from .code_280 import sequential_search


def test():
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)