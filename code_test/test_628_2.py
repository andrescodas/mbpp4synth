from .code_628 import *
from .code_628 import replace_spaces


def test():
    assert replace_spaces("I love Coding") == 'I%20love%20Coding'