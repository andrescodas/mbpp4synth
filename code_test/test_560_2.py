from .code_560 import *
from .code_560 import union_elements


def test():
    assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)