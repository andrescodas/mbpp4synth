from .code_490 import *
from .code_490 import extract_symmetric


def test():
    assert extract_symmetric([(7, 8), (3, 4), (8, 7), (10, 9), (11, 3), (9, 10)] ) == {(9, 10), (7, 8)}