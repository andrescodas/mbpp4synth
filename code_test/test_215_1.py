from .code_215 import *
from .code_215 import decode_list


def test():
    assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']