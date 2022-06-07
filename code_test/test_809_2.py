from .code_809 import *
from .code_809 import check_smaller


def test():
    assert check_smaller((11, 12, 13), (10, 11, 12)) == True