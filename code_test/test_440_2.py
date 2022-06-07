from .code_440 import *
from .code_440 import find_adverb_position


def test():
    assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')