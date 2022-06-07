from .code_288 import *
from .code_288 import modular_inverse


def test():
    assert modular_inverse([ 1, 6, 4, 5 ], 4, 7) == 2