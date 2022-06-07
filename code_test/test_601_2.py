from .code_601 import *
from .code_601 import max_chain_length


def test():
    assert max_chain_length([Pair(19, 10), Pair(11, 12),Pair(13, 14), Pair(15, 16), Pair(31, 54)], 5) == 5