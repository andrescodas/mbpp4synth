from .code_262 import *
from .code_262 import split_two_parts


def test():
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])