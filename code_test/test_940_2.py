from .code_940 import *
from .code_940 import heap_sort


def test():
    assert heap_sort([21, 15, 29, 78, 65]) == [15, 21, 29, 65, 78]