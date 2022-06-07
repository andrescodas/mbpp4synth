from .code_417 import *
from .code_417 import group_tuples


def test():
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]