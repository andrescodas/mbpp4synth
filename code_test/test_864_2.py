from .code_864 import *
from .code_864 import palindrome_lambda


def test():
    assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']