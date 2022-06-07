from .code_280 import *
from .code_280 import sequential_search


def test():
    assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)