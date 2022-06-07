from .code_2 import *
from .code_2 import similar_elements


def test():
    assert similar_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)