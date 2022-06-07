from .code_691 import *
from .code_691 import group_element


def test():
    assert group_element([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}