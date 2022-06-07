from .code_603 import *
from .code_603 import get_ludic


def test():
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]