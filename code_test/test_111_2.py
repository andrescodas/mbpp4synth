from .code_111 import *
from .code_111 import common_in_nested_lists


def test():
    assert common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]])==[4]