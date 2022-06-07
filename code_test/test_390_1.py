from .code_390 import *
from .code_390 import add_string


def test():
    assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']