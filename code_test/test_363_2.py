from .code_363 import *
from .code_363 import add_K_element


def test():
    assert add_K_element([(11, 12, 13), (14, 15, 16), (17, 18, 19)], 9) == [(20, 21, 22), (23, 24, 25), (26, 27, 28)]