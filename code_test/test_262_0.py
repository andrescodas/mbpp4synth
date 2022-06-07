from .code_262 import *
from .code_262 import split_two_parts


def test():
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])