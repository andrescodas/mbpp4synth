from .code_631 import *
from .code_631 import replace_spaces


def test():
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'