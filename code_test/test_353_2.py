from .code_353 import *
from .code_353 import remove_column


def test():
    assert remove_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[[3], [7], [3], [15, 17], [7], [11]]