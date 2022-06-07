from .code_219 import *
from .code_219 import extract_min_max


def test():
    assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)