from .code_368 import *
from .code_368 import repeat_tuples


def test():
    assert repeat_tuples((1, 2), 3) == ((1, 2), (1, 2), (1, 2))