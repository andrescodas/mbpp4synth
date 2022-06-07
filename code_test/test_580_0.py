from .code_580 import *
from .code_580 import extract_even


def test():
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)