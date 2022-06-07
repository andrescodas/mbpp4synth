from .code_892 import *
from .code_892 import remove_spaces


def test():
    assert remove_spaces('python  program')==('python program')