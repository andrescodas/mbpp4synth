from .code_111 import *
from .code_111 import common_in_nested_lists


def test():
    assert common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])==[5,23]