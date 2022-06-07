from .code_205 import *
from .code_205 import inversion_elements


def test():
    assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)