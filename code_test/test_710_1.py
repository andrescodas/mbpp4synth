from .code_710 import *
from .code_710 import front_and_rear


def test():
    assert front_and_rear((1, 2, 3, 4, 5)) == (1, 5)