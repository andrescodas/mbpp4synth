from .code_894 import *
from .code_894 import float_to_tuple


def test():
    assert float_to_tuple("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)