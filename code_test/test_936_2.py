from .code_936 import *
from .code_936 import re_arrange_tuples


def test():
    assert re_arrange_tuples([(6, 3), (3, 8), (5, 7), (2, 4)],  [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]