from .code_333 import *
from .code_333 import Sort


def test():
    assert Sort([['452', 10], ['256', 5], ['100', 20], ['135', 15]]) == [['256', 5], ['452', 10], ['135', 15], ['100', 20]]