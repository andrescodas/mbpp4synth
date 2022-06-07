from .code_16 import *
from .code_16 import text_lowercase_underscore


def test():
    assert text_lowercase_underscore("Aaab_abbbc")==('Not matched!')