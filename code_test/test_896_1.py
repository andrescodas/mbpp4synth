from .code_896 import *
from .code_896 import sort_list_last


def test():
    assert sort_list_last([(9,8), (4, 7), (3,5), (7,9), (1,2)])==[(1,2), (3,5), (4,7), (9,8), (7,9)] 