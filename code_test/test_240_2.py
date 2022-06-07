from .code_240 import *
from .code_240 import replace_list


def test():
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]