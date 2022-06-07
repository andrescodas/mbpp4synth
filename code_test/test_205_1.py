from .code_205 import *
from .code_205 import inversion_elements


def test():
    assert inversion_elements((2, 4, 5, 6, 1, 7)) == (-3, -5, -6, -7, -2, -8)