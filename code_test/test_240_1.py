from .code_240 import *
from .code_240 import replace_list


def test():
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]