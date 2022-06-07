from .code_219 import *
from .code_219 import extract_min_max


def test():
    assert extract_min_max((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)