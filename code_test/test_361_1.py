from .code_361 import *
from .code_361 import remove_empty


def test():
    assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']