from .code_715 import *
from .code_715 import str_to_tuple


def test():
    assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)