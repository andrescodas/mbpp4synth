from .code_586 import *
from .code_586 import split_Arr


def test():
    assert split_Arr([12,10,5,6,52,36],6,2) == [5,6,52,36,12,10]