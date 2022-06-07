from .code_186 import *
from .code_186 import check_literals


def test():
    assert check_literals('The quick brown fox jumps over the lazy dog.',['horse']) == 'Not Matched!'