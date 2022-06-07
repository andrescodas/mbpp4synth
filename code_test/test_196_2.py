from .code_196 import *
from .code_196 import remove_tuples


def test():
    assert remove_tuples([(1, 4, 4), (4, 3), (8, 6, 7), (1, ), (3, 6, 7)] , 3) == [(4, 3), (1,)]