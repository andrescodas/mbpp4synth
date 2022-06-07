from .code_130 import *
from .code_130 import max_occurrences


def test():
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)