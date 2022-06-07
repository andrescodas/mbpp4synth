from .code_263 import *
from .code_263 import merge_dict


def test():
    assert merge_dict({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}