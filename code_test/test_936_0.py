from .code_936 import *
from .code_936 import re_arrange_tuples


def test():
    assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)],  [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]