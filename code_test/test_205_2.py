from .code_205 import *
from .code_205 import inversion_elements


def test():
    assert inversion_elements((8, 9, 11, 14, 12, 13)) == (-9, -10, -12, -15, -13, -14)