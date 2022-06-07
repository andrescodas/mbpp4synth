from .code_769 import *
from .code_769 import Diff


def test():
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]