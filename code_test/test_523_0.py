from .code_523 import *
from .code_523 import check_string


def test():
    assert check_string('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']