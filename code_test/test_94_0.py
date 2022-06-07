from .code_94 import *
from .code_94 import index_minimum


def test():
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'