from .code_417 import *
from .code_417 import group_tuples


def test():
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]