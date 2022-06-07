from .code_368 import *
from .code_368 import repeat_tuples


def test():
    assert repeat_tuples((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))