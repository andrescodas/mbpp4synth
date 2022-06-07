from .code_949 import *
from .code_949 import sort_list


def test():
    assert sort_list([(3, 4, 8), (1, 2), (1234335,), (1345, 234, 334)] ) == '[(1, 2), (3, 4, 8), (1234335,), (1345, 234, 334)]'