from .code_110 import *
from .code_110 import extract_missing


def test():
    assert extract_missing([(6, 9), (15, 34), (48, 70)], 2, 100) == [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]