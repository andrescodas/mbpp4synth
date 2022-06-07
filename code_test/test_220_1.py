from .code_220 import *
from .code_220 import replace_max_specialchar


def test():
    assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')