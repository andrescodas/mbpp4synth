from .code_839 import *
from .code_839 import sort_tuple


def test():
    assert sort_tuple([("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]) == [('aa', 30), ('aaaa', 28), ('bab', 29), ('bb', 21), ('csa', 'C')]