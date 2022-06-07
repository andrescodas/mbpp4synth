from .code_693 import *
from .code_693 import remove_multiple_spaces


def test():
    assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'