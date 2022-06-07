from .code_374 import *
from .code_374 import permute_string


def test():
    assert permute_string('abc')==['abc', 'bac', 'bca', 'acb', 'cab', 'cba']