from .code_665 import *
from .code_665 import move_last


def test():
    assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]