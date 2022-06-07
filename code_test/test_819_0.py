from .code_819 import *
from .code_819 import count_duplic


def test():
    assert count_duplic([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])