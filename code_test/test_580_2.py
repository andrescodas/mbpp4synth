from .code_580 import *
from .code_580 import extract_even


def test():
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)