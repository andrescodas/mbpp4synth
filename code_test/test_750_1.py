from .code_750 import *
from .code_750 import add_tuple


def test():
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]