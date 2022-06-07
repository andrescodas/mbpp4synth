from .code_341 import *
from .code_341 import set_to_tuple


def test():
    assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)