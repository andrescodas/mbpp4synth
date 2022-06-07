from .code_652 import *
from .code_652 import matrix_to_list


def test():
    assert matrix_to_list([[(6, 7), (9, 10)], [(12, 15), (20, 21)], [(23, 7), (15, 8)]]) == '[(6, 9, 12, 20, 23, 15), (7, 10, 15, 21, 7, 8)]'