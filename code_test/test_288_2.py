from .code_288 import *
from .code_288 import modular_inverse


def test():
    assert modular_inverse([2, 3, 4, 5], 4, 6) == 1