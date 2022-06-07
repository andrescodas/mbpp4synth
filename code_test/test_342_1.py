from .code_342 import *
from .code_342 import find_minimum_range


def test():
    assert find_minimum_range([[ 2, 3, 4, 8, 10, 15 ], [1, 5, 12], [7, 8, 15, 16], [3, 6]]) == (4, 7)