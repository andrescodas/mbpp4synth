from .code_769 import *
from .code_769 import Diff


def test():
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]