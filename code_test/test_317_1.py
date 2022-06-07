from .code_317 import *
from .code_317 import modified_encode


def test():
    assert modified_encode('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']