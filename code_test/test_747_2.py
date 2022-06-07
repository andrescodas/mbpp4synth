from .code_747 import *
from .code_747 import lcs_of_three


def test():
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea', 7, 6, 5) == 3