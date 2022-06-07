from .code_930 import *
from .code_930 import text_match


def test():
    assert text_match("abbc") == 'Found a match!'