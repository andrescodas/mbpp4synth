from .code_230 import *
from .code_230 import replace_blank


def test():
    assert replace_blank("blank space","-")==("blank-space")