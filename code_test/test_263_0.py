from .code_263 import *
from .code_263 import merge_dict


def test():
    assert merge_dict({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}