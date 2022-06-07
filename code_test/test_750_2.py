from .code_750 import *
from .code_750 import add_tuple


def test():
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]