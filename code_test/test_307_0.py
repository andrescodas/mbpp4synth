from .code_307 import *
from .code_307 import colon_tuplex


def test():
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 