from .code_754 import *
from .code_754 import extract_index_list


def test():
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]