from .code_580 import *
from .code_580 import extract_even


def test():
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))