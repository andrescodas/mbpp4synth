from .code_839 import *
from .code_839 import sort_tuple


def test():
    assert sort_tuple([("Sarala", 28), ("Ayesha", 30), ("Suman", 29),("Sai", 21), ("G", "H")]) == [('Ayesha', 30), ('G', 'H'), ('Sai', 21), ('Sarala', 28), ('Suman', 29)]