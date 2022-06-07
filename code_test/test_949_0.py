from .code_949 import *
from .code_949 import sort_list


def test():
    assert sort_list([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)] ) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'