from .code_121 import *
from .code_121 import check_triplet


def test():
    assert check_triplet([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0) == False