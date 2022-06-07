from .code_243 import *
from .code_243 import sort_on_occurence


def test():
    assert sort_on_occurence([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]) == [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]