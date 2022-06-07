from .code_972 import *
from .code_972 import concatenate_nested


def test():
    assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)