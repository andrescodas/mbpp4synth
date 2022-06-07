from .code_710 import *
from .code_710 import front_and_rear


def test():
    assert front_and_rear((6, 7, 8, 9, 10)) == (6, 10)