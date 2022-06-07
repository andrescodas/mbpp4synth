from .code_399 import *
from .code_399 import bitwise_xor


def test():
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)