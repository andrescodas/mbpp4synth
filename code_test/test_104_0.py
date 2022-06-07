from .code_104 import *
from .code_104 import sort_sublists


def test():
    assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]