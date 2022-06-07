from .code_43 import *
from .code_43 import text_match


def test():
    assert text_match("Aaab_abbbc") == 'Not matched!'