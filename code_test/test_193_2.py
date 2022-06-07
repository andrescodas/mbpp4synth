from .code_193 import *
from .code_193 import remove_tuple


def test():
    assert remove_tuple((11, 12, 13, 11, 11, 12, 14, 13)) == (11, 12, 13, 14)