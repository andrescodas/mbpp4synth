from .code_157 import *
from .code_157 import encode_list


def test():
    assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]