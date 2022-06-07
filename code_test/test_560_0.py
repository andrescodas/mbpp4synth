from .code_560 import *
from .code_560 import union_elements


def test():
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)