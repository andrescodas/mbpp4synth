from .code_949 import *
from .code_949 import sort_list


def test():
    assert sort_list([(34, 4, 61, 723), (1, 2), (145,), (134, 23)] ) == '[(1, 2), (145,), (134, 23), (34, 4, 61, 723)]'