from .code_154 import *
from .code_154 import specified_element


def test():
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],3)==[2,2,5]