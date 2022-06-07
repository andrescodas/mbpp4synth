from .code_586 import *
from .code_586 import split_Arr


def test():
    assert split_Arr([1,2,3,4],4,1) == [2,3,4,1]