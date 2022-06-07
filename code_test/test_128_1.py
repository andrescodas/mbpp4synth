from .code_128 import *
from .code_128 import long_words


def test():
    assert long_words(2,"writing a program")==['writing','program']