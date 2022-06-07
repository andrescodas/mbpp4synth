from .code_861 import *
from .code_861 import anagram_lambda


def test():
    assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']