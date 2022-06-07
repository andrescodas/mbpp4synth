from .code_323 import *
from .code_323 import re_arrange


def test():
    assert re_arrange([1, 2, 3, -4, -1, 4], 6) == [-4, 1, -1, 2, 3, 4]