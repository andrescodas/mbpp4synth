from .code_825 import *
from .code_825 import access_elements


def test():
    assert access_elements([1, 2, 3, 4, 5],[1,2]) == [2,3]