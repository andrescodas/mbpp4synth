from .code_353 import *
from .code_353 import remove_column


def test():
    assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[[2, 3], [4, 5], [1, 1]]