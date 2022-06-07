from .code_894 import *
from .code_894 import float_to_tuple


def test():
    assert float_to_tuple("0.3, 0.5, 7.8, 9.4") == (0.3, 0.5, 7.8, 9.4)