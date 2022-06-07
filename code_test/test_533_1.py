from .code_533 import *
from .code_533 import remove_datatype


def test():
    assert remove_datatype((7, 8, 9, "SR"), str) == [7, 8, 9]