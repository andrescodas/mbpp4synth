from .code_196 import *
from .code_196 import remove_tuples


def test():
    assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] , 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]