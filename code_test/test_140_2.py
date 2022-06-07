from .code_140 import *
from .code_140 import extract_singly


def test():
    assert extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]