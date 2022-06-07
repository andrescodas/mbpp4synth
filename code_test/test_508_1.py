from .code_508 import *
from .code_508 import same_order


def test():
    assert same_order(["red","pink","green","white","black"],["white","orange","pink","black"])==False