from .code_648 import *
from .code_648 import exchange_elements


def test():
    assert exchange_elements([0,1,2,3,4,5])==[1, 0, 3, 2, 5, 4] 