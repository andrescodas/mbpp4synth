from .code_706 import *
from .code_706 import is_subset


def test():
    assert is_subset([10, 5, 2, 23, 19], 5, [19, 5, 3], 3) == False