from .code_317 import *
from .code_317 import modified_encode


def test():
    assert modified_encode([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]