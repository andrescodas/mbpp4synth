from .code_628 import *
from .code_628 import replace_spaces


def test():
    assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'