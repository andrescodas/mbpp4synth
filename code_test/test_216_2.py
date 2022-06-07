from .code_216 import *
from .code_216 import check_subset_list


def test():
    assert check_subset_list([['a', 'b'], ['e'], ['c', 'd']],[['g']])==False