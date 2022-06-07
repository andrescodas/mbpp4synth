from .code_534 import *
from .code_534 import search_literal


def test():
    assert search_literal('programming','python programming language')==(7,18)