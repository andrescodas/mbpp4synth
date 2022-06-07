from .code_625 import *
from .code_625 import swap_List


def test():
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]