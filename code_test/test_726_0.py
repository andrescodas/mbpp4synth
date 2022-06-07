from .code_726 import *
from .code_726 import multiply_elements


def test():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)