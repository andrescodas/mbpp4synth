from .code_2 import *
from .code_2 import similar_elements


def test():
    assert similar_elements((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)