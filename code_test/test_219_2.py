from .code_219 import *
from .code_219 import extract_min_max


def test():
    assert extract_min_max((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)