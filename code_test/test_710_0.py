from .code_710 import *
from .code_710 import front_and_rear


def test():
    assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)