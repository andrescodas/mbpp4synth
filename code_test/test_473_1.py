from .code_473 import *
from .code_473 import tuple_intersection


def test():
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}