from .code_601 import *
from .code_601 import max_chain_length


def test():
    assert max_chain_length([Pair(1, 2), Pair(3, 4),Pair(5, 6), Pair(7, 8)], 4) == 4