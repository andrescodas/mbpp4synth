from .code_423 import *
from .code_423 import get_maxgold


def test():
    assert get_maxgold([[4,9],[3,7]],2,2)==13