from .code_73 import *
from .code_73 import multiple_split


def test():
    assert multiple_split('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']