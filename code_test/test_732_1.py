from .code_732 import *
from .code_732 import replace_specialchar


def test():
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')