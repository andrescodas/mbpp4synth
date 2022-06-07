from .code_616 import *
from .code_616 import tuple_modulo


def test():
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)