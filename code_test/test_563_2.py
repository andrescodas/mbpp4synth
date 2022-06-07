from .code_563 import *
from .code_563 import extract_values


def test():
    assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']