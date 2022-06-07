from .code_825 import *
from .code_825 import access_elements


def test():
    assert access_elements([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]