from .code_43 import *
from .code_43 import text_match


def test():
    assert text_match("aab-cbbbc") == 'Not matched!'