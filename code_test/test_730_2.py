from .code_730 import *
from .code_730 import consecutive_duplicates


def test():
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']