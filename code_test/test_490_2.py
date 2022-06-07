from .code_490 import *
from .code_490 import extract_symmetric


def test():
    assert extract_symmetric([(8, 9), (4, 5), (9, 8), (11, 10), (12, 4), (10, 11)] ) == {(8, 9), (10, 11)}