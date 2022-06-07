from .code_484 import *
from .code_484 import remove_matching_tuple


def test():
    assert remove_matching_tuple([('Its', 'been'), ('a', 'long'), ('day', 'without')], [('a', 'long'), ('my', 'friend')]) == [('Its', 'been'), ('day', 'without')]