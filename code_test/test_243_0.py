from .code_243 import *
from .code_243 import sort_on_occurence


def test():
    assert sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]