from .code_938 import *
from .code_938 import find_closet


def test():
    assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)