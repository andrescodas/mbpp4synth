from .code_972 import *
from .code_972 import concatenate_nested


def test():
    assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)