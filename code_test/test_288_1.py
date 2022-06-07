from .code_288 import *
from .code_288 import modular_inverse


def test():
    assert modular_inverse([1, 3, 8, 12, 12], 5, 13) == 3