from .code_534 import *
from .code_534 import search_literal


def test():
    assert search_literal('python','python programming language')==(0,6)