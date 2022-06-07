from .code_872 import *
from .code_872 import check_subset


def test():
    assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True