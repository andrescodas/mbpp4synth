from .code_216 import *
from .code_216 import check_subset_list


def test():
    assert check_subset_list([[2, 3, 1], [4, 5], [6, 8]],[[4, 5], [6, 8]])==True