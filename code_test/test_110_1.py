from .code_110 import *
from .code_110 import extract_missing


def test():
    assert extract_missing([(7, 2), (15, 19), (38, 50)], 5, 60) == [(5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)]