from .code_473 import *
from .code_473 import tuple_intersection


def test():
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}