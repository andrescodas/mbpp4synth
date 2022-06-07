from .code_879 import *
from .code_879 import text_match


def test():
    assert text_match("aabAbbbc") == 'Not matched!'