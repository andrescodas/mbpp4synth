from .code_140 import *
from .code_140 import extract_singly


def test():
    assert extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]