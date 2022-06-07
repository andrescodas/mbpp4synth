from .code_307 import *
from .code_307 import colon_tuplex


def test():
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))