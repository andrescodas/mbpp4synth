from .code_110 import *
from .code_110 import extract_missing


def test():
    assert extract_missing([(7, 2), (15, 19), (38, 50)], 1, 52) == [(1, 7), (2, 52), (2, 15), (19, 52), (19, 38), (50, 52)]