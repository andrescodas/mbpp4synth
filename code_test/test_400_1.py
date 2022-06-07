from .code_400 import *
from .code_400 import extract_freq


def test():
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4