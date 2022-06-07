from .code_902 import *
from .code_902 import add_dict


def test():
    assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 