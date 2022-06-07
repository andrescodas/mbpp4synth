from .code_896 import *
from .code_896 import sort_list_last


def test():
    assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])==[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 