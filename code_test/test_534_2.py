from .code_534 import *
from .code_534 import search_literal


def test():
    assert search_literal('language','python programming language')==(19,27)