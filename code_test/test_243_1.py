from .code_243 import *
from .code_243 import sort_on_occurence


def test():
    assert sort_on_occurence([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]) == [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]