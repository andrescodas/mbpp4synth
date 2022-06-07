from .code_951 import *
from .code_951 import max_similar_indices


def test():
    assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]