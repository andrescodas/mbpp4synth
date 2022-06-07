from .code_399 import *
from .code_399 import bitwise_xor


def test():
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)