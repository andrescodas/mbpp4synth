from .code_539 import *
from .code_539 import basesnum_coresspondingnum


def test():
    assert basesnum_coresspondingnum([10, 20, 30, 40, 50, 60, 70, 80, 90, 100],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000, 387420489000000000, 100000000000000000000]