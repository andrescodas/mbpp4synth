from .code_678 import *
from .code_678 import remove_spaces


def test():
    assert remove_spaces("a b c") == "abc"