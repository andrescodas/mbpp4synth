from .code_368 import *
from .code_368 import repeat_tuples


def test():
    assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))