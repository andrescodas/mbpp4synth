from .code_265 import *
from .code_265 import list_split


def test():
    assert list_split([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3)==[[1,4,7,10,13], [2,5,8,11,14], [3,6,9,12]] 