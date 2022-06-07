from .code_652 import *
from .code_652 import matrix_to_list


def test():
    assert matrix_to_list([[(5, 6), (8, 9)], [(11, 14), (19, 18)], [(1, 5), (11, 2)]]) == '[(5, 8, 11, 19, 1, 11), (6, 9, 14, 18, 5, 2)]'