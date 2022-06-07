from .code_523 import *
from .code_523 import check_string


def test():
    assert check_string('123python')==['String must have 1 upper case character.']