from .code_376 import *
from .code_376 import remove_replica


def test():
    assert remove_replica((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')