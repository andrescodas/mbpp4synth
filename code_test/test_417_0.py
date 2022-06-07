from .code_417 import *
from .code_417 import group_tuples


def test():
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]