from .code_773 import *
from .code_773 import occurance_substring


def test():
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)