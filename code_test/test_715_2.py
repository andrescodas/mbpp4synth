from .code_715 import *
from .code_715 import str_to_tuple


def test():
    assert str_to_tuple("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)