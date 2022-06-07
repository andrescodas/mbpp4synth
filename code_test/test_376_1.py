from .code_376 import *
from .code_376 import remove_replica


def test():
    assert remove_replica((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)) == (2, 3, 4, 'MSP', 5, 6, 'MSP', 7, 8, 9, 'MSP')