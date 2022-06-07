from .code_852 import *
from .code_852 import remove_negs


def test():
    assert remove_negs([4,5,-6,7,-8]) == [4,5,7]