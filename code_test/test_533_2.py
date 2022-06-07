from .code_533 import *
from .code_533 import remove_datatype


def test():
    assert remove_datatype((7, 1.1, 2, 2.2), float) == [7, 2]