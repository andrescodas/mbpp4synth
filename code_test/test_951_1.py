from .code_951 import *
from .code_951 import max_similar_indices


def test():
    assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]