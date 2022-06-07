from .code_815 import *
from .code_815 import sort_by_dnf


def test():
    assert sort_by_dnf([2,2,1,0,0,0,1,1,2,1], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]