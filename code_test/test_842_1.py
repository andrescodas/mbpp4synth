from .code_842 import *
from .code_842 import get_odd_occurence


def test():
    assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3