from .code_938 import *
from .code_938 import find_closet


def test():
    assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)