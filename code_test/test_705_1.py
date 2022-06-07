from .code_705 import *
from .code_705 import sort_sublists


def test():
    assert sort_sublists([[1], [2, 3], [4, 5, 6], [7], [10, 11]])==[[1], [7], [2, 3], [10, 11], [4, 5, 6]]