from .code_2 import *
from .code_2 import similar_elements


def test():
    assert similar_elements((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)