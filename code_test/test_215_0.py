from .code_215 import *
from .code_215 import decode_list


def test():
    assert decode_list([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]