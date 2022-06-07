from .code_323 import *
from .code_323 import re_arrange


def test():
    assert re_arrange([-5, -2, 5, 2, 4,	7, 1, 8, 0, -8], 10) == [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]