from .code_780 import *
from .code_780 import find_combinations


def test():
    assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]