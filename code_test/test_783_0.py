from .code_783 import *
from .code_783 import rgb_to_hsv


def test():
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)