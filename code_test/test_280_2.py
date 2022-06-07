from .code_280 import *
from .code_280 import sequential_search


def test():
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)