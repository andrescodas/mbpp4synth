from .code_665 import *
from .code_665 import move_last


def test():
    assert move_last([5,4,3,2,1]) == [4,3,2,1,5]