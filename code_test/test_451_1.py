from .code_451 import *
from .code_451 import remove_whitespaces


def test():
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'