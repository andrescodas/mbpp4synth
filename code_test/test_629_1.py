from .code_629 import *
from .code_629 import Split


def test():
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]