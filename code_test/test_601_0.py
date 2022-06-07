from .code_601 import *
from .code_601 import max_chain_length


def test():
    assert max_chain_length([Pair(5, 24), Pair(15, 25),Pair(27, 40), Pair(50, 60)], 4) == 3