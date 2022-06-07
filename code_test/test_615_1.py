from .code_615 import *
from .code_615 import average_tuple


def test():
    assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]