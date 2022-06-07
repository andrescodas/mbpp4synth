from .code_800 import *
from .code_800 import remove_all_spaces


def test():
    assert remove_all_spaces('python                     program')==('pythonprogram')