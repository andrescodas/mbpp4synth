from .code_533 import *
from .code_533 import remove_datatype


def test():
    assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]