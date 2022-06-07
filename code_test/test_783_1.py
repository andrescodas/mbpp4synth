from .code_783 import *
from .code_783 import rgb_to_hsv


def test():
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)