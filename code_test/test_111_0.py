from .code_111 import *
from .code_111 import common_in_nested_lists


def test():
    assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])==[18, 12]