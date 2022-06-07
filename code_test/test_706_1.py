from .code_706 import *
from .code_706 import is_subset


def test():
    assert is_subset([1, 2, 3, 4, 5, 6], 6, [1, 2, 4], 3) == True