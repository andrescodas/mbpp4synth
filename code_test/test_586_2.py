from .code_586 import *
from .code_586 import split_Arr


def test():
    assert split_Arr([0,1,2,3,4,5,6,7],8,3) == [3,4,5,6,7,0,1,2]