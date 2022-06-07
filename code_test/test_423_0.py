from .code_423 import *
from .code_423 import get_maxgold


def test():
    assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16