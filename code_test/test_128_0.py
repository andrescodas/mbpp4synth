from .code_128 import *
from .code_128 import long_words


def test():
    assert long_words(3,"python is a programming language")==['python','programming','language']