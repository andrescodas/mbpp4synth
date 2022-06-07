from .code_500 import *
from .code_500 import concatenate_elements


def test():
    assert concatenate_elements([ 'Part', 'of', 'the','journey', 'is', 'end'] ) == '  Part of the journey is end'