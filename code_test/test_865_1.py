from .code_865 import *
from .code_865 import ntimes_list


def test():
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]