from .code_503 import *
from .code_503 import add_consecutive_nums


def test():
    assert add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[3, 5, 7, 9, 11, 13, 15, 17, 19]