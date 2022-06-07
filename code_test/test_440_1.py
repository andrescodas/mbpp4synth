from .code_440 import *
from .code_440 import find_adverb_position


def test():
    assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')