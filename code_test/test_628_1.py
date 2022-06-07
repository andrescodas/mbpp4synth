from .code_628 import *
from .code_628 import replace_spaces


def test():
    assert replace_spaces("I am a Programmer") == 'I%20am%20a%20Programmer'