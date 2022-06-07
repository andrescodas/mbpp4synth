from .code_27 import *
from .code_27 import remove


def test():
    assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']