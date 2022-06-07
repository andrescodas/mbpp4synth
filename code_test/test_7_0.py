from .code_7 import *
from .code_7 import find_char_long


def test():
    assert find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']