from .code_665 import *
from .code_665 import move_last


def test():
    assert move_last([1,2,3,4]) == [2,3,4,1]