from .code_210 import *
from .code_210 import is_allowed_specific_char


def test():
    assert is_allowed_specific_char("*&%@#!}{") == False