from .code_715 import *
from .code_715 import str_to_tuple


def test():
    assert str_to_tuple("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)