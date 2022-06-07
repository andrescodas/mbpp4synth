from .code_659 import *
from .code_659 import Repeat


def test():
    assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]