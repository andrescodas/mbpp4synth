from .code_778 import *
from .code_778 import pack_consecutive_duplicates


def test():
    assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]