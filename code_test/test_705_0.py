from .code_705 import *
from .code_705 import sort_sublists


def test():
    assert sort_sublists([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]])==[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]