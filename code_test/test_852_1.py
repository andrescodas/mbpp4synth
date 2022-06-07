from .code_852 import *
from .code_852 import remove_negs


def test():
    assert remove_negs([1,2,3,-4]) == [1,2,3]