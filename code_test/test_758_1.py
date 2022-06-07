from .code_758 import *
from .code_758 import unique_sublists


def test():
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}