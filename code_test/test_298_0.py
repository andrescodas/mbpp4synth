from .code_298 import *
from .code_298 import intersection_nested_lists


def test():
    assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]