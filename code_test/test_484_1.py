from .code_484 import *
from .code_484 import remove_matching_tuple


def test():
    assert remove_matching_tuple([('Part', 'of'), ('the', 'journey'), ('is ', 'end')], [('Journey', 'the'), ('is', 'end')]) == [('Part', 'of'), ('the', 'journey'), ('is ', 'end')]