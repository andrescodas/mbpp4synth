from .code_428 import *
from .code_428 import shell_sort


def test():
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]