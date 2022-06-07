from .code_706 import *
from .code_706 import is_subset


def test():
    assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True