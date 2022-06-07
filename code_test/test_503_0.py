from .code_503 import *
from .code_503 import add_consecutive_nums


def test():
    assert add_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[2, 4, 7, 8, 9, 11, 13]