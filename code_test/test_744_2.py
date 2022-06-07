from .code_744 import *
from .code_744 import check_none


def test():
    assert check_none((1, 2, 3, 4, None)) == True