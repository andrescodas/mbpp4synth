from .code_869 import *
from .code_869 import remove_list_range


def test():
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]