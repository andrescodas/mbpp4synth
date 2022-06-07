from .code_951 import *
from .code_951 import max_similar_indices


def test():
    assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]