from .code_140 import *
from .code_140 import extract_singly


def test():
    assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]