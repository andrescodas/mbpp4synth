from .code_569 import *
from .code_569 import sort_sublists


def test():
    assert sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']])==[['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]