from .code_560 import *
from .code_560 import union_elements


def test():
    assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)