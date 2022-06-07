from .code_616 import *
from .code_616 import tuple_modulo


def test():
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)