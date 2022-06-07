from .code_894 import *
from .code_894 import float_to_tuple


def test():
    assert float_to_tuple("2.3, 2.4, 5.6, 5.4, 8.9") == (2.3, 2.4, 5.6, 5.4, 8.9)