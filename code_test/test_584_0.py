from .code_584 import *
from .code_584 import find_adverbs


def test():
    assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'