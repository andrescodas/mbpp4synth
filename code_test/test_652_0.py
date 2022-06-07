from .code_652 import *
from .code_652 import matrix_to_list


def test():
    assert matrix_to_list([[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]) == '[(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]'