from .code_400 import *
from .code_400 import extract_freq


def test():
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3