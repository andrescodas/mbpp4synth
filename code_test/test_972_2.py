from .code_972 import *
from .code_972 import concatenate_nested


def test():
    assert concatenate_nested((4, 5), (6, 8)) == (4, 5, 6, 8)