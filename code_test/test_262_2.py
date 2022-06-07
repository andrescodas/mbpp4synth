from .code_262 import *
from .code_262 import split_two_parts


def test():
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])