from .code_691 import *
from .code_691 import group_element


def test():
    assert group_element([(7, 6), (3, 8), (3, 6), (9, 8), (10, 9), (4, 8)]) == {6: [7, 3], 8: [3, 9, 4], 9: [10]}