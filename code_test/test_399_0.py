from .code_399 import *
from .code_399 import bitwise_xor


def test():
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)