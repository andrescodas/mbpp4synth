from .code_842 import *
from .code_842 import get_odd_occurence


def test():
    assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5