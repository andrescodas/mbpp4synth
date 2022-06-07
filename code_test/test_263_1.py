from .code_263 import *
from .code_263 import merge_dict


def test():
    assert merge_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}