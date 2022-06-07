from .code_333 import *
from .code_333 import Sort


def test():
    assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]