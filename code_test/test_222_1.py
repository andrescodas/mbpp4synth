from .code_222 import *
from .code_222 import check_type


def test():
    assert check_type((1, 2, "4") ) == False