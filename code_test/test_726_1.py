from .code_726 import *
from .code_726 import multiply_elements


def test():
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)