from .code_376 import *
from .code_376 import remove_replica


def test():
    assert remove_replica((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)) == (2, 'MSP', 5, 4, 'MSP', 7, 'MSP', 6, 'MSP', 'MSP')