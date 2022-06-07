from .code_693 import *
from .code_693 import remove_multiple_spaces


def test():
    assert remove_multiple_spaces('Quad      Core') == 'Quad Core'