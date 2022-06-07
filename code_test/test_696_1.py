from .code_696 import *
from .code_696 import zip_list


def test():
    assert zip_list([[1, 2], [3, 4], [5, 6]] ,[[7, 8], [9, 10], [11, 12]] )==[[1, 2, 7, 8], [3, 4, 9, 10], [5, 6, 11, 12]]