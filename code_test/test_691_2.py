from .code_691 import *
from .code_691 import group_element


def test():
    assert group_element([(8, 7), (4, 9), (4, 7), (10, 9), (11, 10), (5, 9)]) == {7: [8, 4], 9: [4, 10, 5], 10: [11]}