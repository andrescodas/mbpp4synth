from .code_943 import *
from .code_943 import combine_lists


def test():
    assert combine_lists([1, 3, 5, 7, 9, 11],[0, 2, 4, 6, 8, 10])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]