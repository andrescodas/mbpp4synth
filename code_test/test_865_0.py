from .code_865 import *
from .code_865 import ntimes_list


def test():
    assert ntimes_list([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]