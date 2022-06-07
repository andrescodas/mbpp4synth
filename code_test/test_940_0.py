from .code_940 import *
from .code_940 import heap_sort


def test():
    assert heap_sort([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]