from .code_631 import *
from .code_631 import replace_spaces


def test():
    assert replace_spaces('The Avengers') == 'The_Avengers'