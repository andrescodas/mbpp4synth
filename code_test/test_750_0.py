from .code_750 import *
from .code_750 import add_tuple


def test():
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]