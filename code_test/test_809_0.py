from .code_809 import *
from .code_809 import check_smaller


def test():
    assert check_smaller((1, 2, 3), (2, 3, 4)) == False