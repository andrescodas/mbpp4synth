from .code_766 import *
from .code_766 import pair_wise


def test():
    assert pair_wise([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]