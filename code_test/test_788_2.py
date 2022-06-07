from .code_788 import *
from .code_788 import new_tuple


def test():
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')