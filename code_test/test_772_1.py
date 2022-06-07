from .code_772 import *
from .code_772 import remove_length


def test():
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'