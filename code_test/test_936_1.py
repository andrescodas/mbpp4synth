from .code_936 import *
from .code_936 import re_arrange_tuples


def test():
    assert re_arrange_tuples([(5, 4), (2, 10), (3, 11), (4, 3)],  [3, 4, 2, 3]) == [(3, 11), (4, 3), (2, 10), (3, 11)]