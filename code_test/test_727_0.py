from .code_727 import *
from .code_727 import remove_char


def test():
    assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'