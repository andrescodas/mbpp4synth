from .code_341 import *
from .code_341 import set_to_tuple


def test():
    assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)