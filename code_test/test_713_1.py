from .code_713 import *
from .code_713 import check_valid


def test():
    assert check_valid((True, False, True, True) ) == False