from .code_819 import *
from .code_819 import count_duplic


def test():
    assert count_duplic([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])