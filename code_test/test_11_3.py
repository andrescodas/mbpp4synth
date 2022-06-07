from .code_11 import *
from .code_11 import remove_Occ


def test():
    assert remove_Occ("hellolloll","l") == "helollol"