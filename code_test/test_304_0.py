from .code_304 import *
from .code_304 import find_Element


def test():
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3