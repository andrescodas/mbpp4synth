from .code_26 import *
from .code_26 import check_k_elements


def test():
    assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True