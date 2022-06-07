from .code_428 import *
from .code_428 import shell_sort


def test():
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]