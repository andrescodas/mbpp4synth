from .code_938 import *
from .code_938 import find_closet


def test():
    assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)