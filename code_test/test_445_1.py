from .code_445 import *
from .code_445 import index_multiplication


def test():
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))