from .code_902 import *
from .code_902 import add_dict


def test():
    assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})