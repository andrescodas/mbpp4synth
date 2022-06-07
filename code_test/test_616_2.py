from .code_616 import *
from .code_616 import tuple_modulo


def test():
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)