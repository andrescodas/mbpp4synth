from .code_484 import *
from .code_484 import remove_matching_tuple


def test():
    assert remove_matching_tuple([('Hello', 'dude'), ('How', 'are'), ('you', '?')], [('Hello', 'dude'), ('How', 'are')]) == [('you', '?')]