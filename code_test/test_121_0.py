from .code_121 import *
from .code_121 import check_triplet


def test():
    assert check_triplet([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True