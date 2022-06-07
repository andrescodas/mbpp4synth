from .code_400 import *
from .code_400 import extract_freq


def test():
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4