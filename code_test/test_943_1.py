from .code_943 import *
from .code_943 import combine_lists


def test():
    assert combine_lists([1, 3, 5, 6, 8, 9], [2, 5, 7, 11])==[1,2,3,5,5,6,7,8,9,11]