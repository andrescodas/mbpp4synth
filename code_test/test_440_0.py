from .code_440 import *
from .code_440 import find_adverb_position


def test():
    assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')