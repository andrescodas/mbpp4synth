from .code_380 import *
from .code_380 import multi_list


def test():
    assert multi_list(5,7)==[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6], [0, 2, 4, 6, 8, 10, 12], [0, 3, 6, 9, 12, 15, 18], [0, 4, 8, 12, 16, 20, 24]]