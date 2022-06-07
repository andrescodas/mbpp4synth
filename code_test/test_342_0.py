from .code_342 import *
from .code_342 import find_minimum_range


def test():
    assert find_minimum_range([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]) == (4, 6)