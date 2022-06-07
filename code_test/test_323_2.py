from .code_323 import *
from .code_323 import re_arrange


def test():
    assert re_arrange([4, 7, 9, 77, -4, 5, -3, -9], 8) == [-4, 4, -3, 7, -9, 9, 77, 5]