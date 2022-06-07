from .code_872 import *
from .code_872 import check_subset


def test():
    assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True