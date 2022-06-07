from .code_727 import *
from .code_727 import remove_char


def test():
    assert remove_char("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'