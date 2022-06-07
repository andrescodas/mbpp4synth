from .code_490 import *
from .code_490 import extract_symmetric


def test():
    assert extract_symmetric([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] ) == {(8, 9), (6, 7)}