from .code_893 import *
from .code_893 import Extract


def test():
    assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']