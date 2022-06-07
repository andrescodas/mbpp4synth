from .code_842 import *
from .code_842 import get_odd_occurence


def test():
    assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5