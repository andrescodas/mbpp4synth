from .code_259 import *
from .code_259 import maximize_elements


def test():
    assert maximize_elements(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((7, 8), (5, 10), (3, 10), (8, 11))