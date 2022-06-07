from .code_780 import *
from .code_780 import find_combinations


def test():
    assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]