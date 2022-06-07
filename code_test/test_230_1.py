from .code_230 import *
from .code_230 import replace_blank


def test():
    assert replace_blank("python program language",'$')==("python$program$language")