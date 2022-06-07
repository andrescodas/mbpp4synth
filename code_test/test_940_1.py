from .code_940 import *
from .code_940 import heap_sort


def test():
    assert heap_sort([32, 14, 5, 6, 7, 19]) == [5, 6, 7, 14, 19, 32]