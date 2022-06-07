from .code_423 import *
from .code_423 import get_maxgold


def test():
    assert get_maxgold([[10,20],[30,40]],2,2)==70